# Generating Compiled Kilosort3 Docker Image

## 1. Kilosort Setup
- Git clone or Download kilosort [source code](https://github.com/MouseLand/Kilosort)
- Git clone or Download spikeinterface [source code](https://github.com/SpikeInterface/spikeinterface)

## 2. Create base image
`compile.sh` script generates the base docker image (called `ks3-matlab-base`) with the matlab compiled Kilosort3 application
- Run compile script:
```bash
$ source compile.sh /path/to/Kilosort /path/to/spikeinterface
```

## 3. Extending Base Image and creating final image

The Dockerfile in this folder applies some fixes and updates to the base image in order to properly run kilosort3:

- In your terminal, go to the folder for this project:
```bash
$ cd /path/to/spikeinterface-dockerfiles/kilosort_no_license/kilosort3-compiled
```

- Run build script:
```bash
$ source build.sh
```
