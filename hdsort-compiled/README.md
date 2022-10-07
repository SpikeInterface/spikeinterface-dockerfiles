# HDsort Compiled Docker Image

This documentation is intended to show how to create a Docker image with Matlab compiled HDsort sorter. The main goal of this project is to avoid the requirement of Matlab Licenses and also abstract the installation and setup steps to run the sorter

There are three main steps for generating a functional HDsort docker image:
1. Compile HDsort as Matlab's Standalone Application
2. Create a base docker image with Matlab Runtime and the compiled application from step 1
3. Extend the docker image from step 2 for improvements and fixes

Steps 1 and 2 are done by `compile.sh` script, while step 3 is done by `build.sh` script

## Requirements
- Packaging a MATLAB Docker image is supported on Linux only
- Docker
- Matlab

### Matlab Requirements
- MATLAB Compiler
- Fuzzy_Logic Toolbox
- More requirements to be checked and listed...

## Cloning repositories
- Git clone or Download HDsort [source code](https://git.bsse.ethz.ch/hima_public/HDsort)
- Git clone or Download spikeinterface [source code](https://github.com/SpikeInterface/spikeinterface)

## Generating Base Docker Image
`compile.sh` script generates the base docker image (called `hdsort-matlab-base`) with the matlab compiled HDSort application
- Run compile script:
```bash
$ source compile.sh /path/to/HDSort /path/to/spikeinterface
```

## Extending Base Image and creating final image
The Dockerfile in this folder applies some fixes and updates to the base image in order to properly run HDSort:

- In your terminal, go to the  folder for this project:
```
$ cd /path/to/spikeinterface-dockerfiles/hdsort-compiled
```

- Run build script:
```
$ source build.sh
```
