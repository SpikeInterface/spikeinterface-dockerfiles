# Ironclust Docker Image

This documentation is intended to show how to create a Docker image with Matlab compiled implementation of Ironclust sorter. The main goal of this project is to avoid the requirement of Matlab Licenses in order to run ironclust.

There are three main steps for generating a functional ironclust docker image:
1. Compile Ironclust as Matlab's Standalone Application
2. Create a base docker image with Matlab Runtime and the compiled application from step 1
3. Extend the docker image from step 2 for improvements and fixes

## Requirements
- Packaging a MATLAB Docker image is supported on Linux only
- Docker
- Matlab

### Matlab Requirements
- JSONLab toolbox
- MATLAB Compiler
- Statistics and Machine Learning Toolbox
- Signal Processing Toolbox
- Image Processing Toolbox

Licenses for Matlab and toolboxes are needed only for compiling ironclust as Standalone Application and to generate the base Docker image. After this process, no license will be required, either to extend the base image or to run the sorter.

## Cloning repositories
- Git clone or Download ironclust [source code](https://github.com/flatironinstitute/ironclust.git)
- Git clone or Download spikeinterface [source code](https://github.com/SpikeInterface/spikeinterface)


## Generating Base Docker Image
`compile.sh` script generates the base docker image (called `ironclust-matlab-base`) with the matlab compiled ironclust application
- Run compile script:
```bash
$ source compile.sh /path/to/ironclust /path/to/spikeinterface
```

## Extending Base Image/Creating final image
The Dockerfile in this folder applies some fixes and updates to the base image in order to properly run ironclust:

- In your terminal, go to the  folder for this project:
```
$ cd /path/to/spikeinterface-dockerfiles/ironclust-compiled
```

- Run build script:
```
$ source build.sh
```

## Running a container

- [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit) is required to run a docker with GPU capabilities

The base syntax to run dockerized ironclust is:

```
docker run -v <host-data-folder>:<docker-data-folder> -it spikeinterface/ironclust p_ironclust [ARGS]
```

Notice that a volume has to be binded to a folder were your data locally is stored

Sample run:
```
docker run -v /home/user/data:/opt/data -it spikeinterface/ironclust p_ironclust /opt/data/tmp /opt/data/raw.mda /opt/data/geom.csv '' '' /opt/data/tmp/firing.mda /opt/data/argfile.txt
```
