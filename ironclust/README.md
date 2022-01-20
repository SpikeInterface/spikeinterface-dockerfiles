# Ironclust Docker Image

This documentation is intended to show how to create a Docker Image with Matlab compiled implementation of ironclust sorter. The main goal of this project is to avoid the requirement of Matlab Licenses in order to run ironclust.

There are three main steps for generating a functional ironclust docker image:
1. Compile Ironclust as Matlab's Standalone Application
2. Create a (base) docker image with Matlab Runtime and the compiled application from step 1
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

Licenses for Matlab and toolboxes are needed only for compiling ironclust as Standalone Application and to generate the base docker image. After this process, no license will be required, either to extend the base image or to run the sorter.


## Compiling Ironclust as Matlab's Standalone Application

- Git clone or Download ironclust [source code](https://github.com/flatironinstitute/ironclust.git)
- Open Matlab
- Set Matlab's workspace folder to: `<local-path-to-project>/ironclust/matlab`
- Open Matlab's `Application Compiler` (located in `APPS` Tab)
- Click on `+` sign in Add Main File, Select `p_ironclust.m` and Click Open
- In `Files installed for your end user` section, Click on `+` sign button and Select all files (some might not be needed, but further tests are needed), also select the following folders:  `prb`, `prb_json`. Click Open
- On Application Compiler window, Click on Package, Save the `p_ironclust.prj` file and wait for Matlab to Compile the project. A folder (named `p_ironclust` by default) with compiled files will be generated.


## Generating Base Docker Image
- Close `Package` and `Application Compiler` windows
- In matlab console run:
```
compiler.package.docker('p_ironclust/for_testing/p_ironclust', 'p_ironclust/for_testing/requiredMCRProducts.txt', 'ImageName', 'ironclust-base')
```

## Extending Base Image/Creating final image
The Dockerfile in this folder applies some fixes and updates to the base image generated automatically by Matlab in order to properly run ironclust:

- In your terminal, go to the current folder:
```
$ cd <local-path-to-project>/spikeinterface-dockerfiles/ironclust
```

- Run docker build:
```
$ docker build -t spikeinterface/ironclust .
```


## Running a container

The base syntax to run dockerized ironclust is:

```
docker run -v <host-data-folder>:<docker-data-folder> -it spikeinterface/ironclust p_ironclust [ARGS]
```

Notice that a volume has to be binded to a folder were your data locally is stored

Sample run:
```
docker run -v /home/user/data:/opt/data -it spikeinterface/ironclust p_ironclust /opt/data/raw.mda /opt/data/geom.csv '' '' /opt/data/tmp/firing.mda /opt/data/argfile.txt
```

