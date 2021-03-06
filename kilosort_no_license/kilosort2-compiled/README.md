# Generating Compiled Kilosort2 Docker Image

## 1. Kilosort Setup 
- Git clone or Download Kilosort [source code](https://github.com/MouseLand/Kilosort)
- Git checkout to the correct version:
```bash
$ git checkout tags/v2.0
```
- Open Matlab
- Compile Kilosort mexfiles:
  - Set Matlab's workspace folder to `<git-cloned-path>/Kilosort/CUDA`
  - In Matlab console run:
    ```matlab
    >> mexGPUall
    ```

## 2. Compiling Kilosort as Matlab's Standalone Application
- Set Matlab's workspace folder to `/path/to/spikeinterface-dockerfiles/kilosort_no_license`
- Run `mcc` command with `utils` folder and kilosort path:
```matlab
>> mcc -m kilosort2-compiled/ks2_compiled.m -a utils -a <git-cloned-path>/Kilosort
```

## 3. Generating Base Docker Image
- To generate the base docker image (called `ks2-matlab-base`) with the compiled application, run the following command in Matlab console:
```matlab
>> compiler.package.docker('ks2_compiled', 'requiredMCRProducts.txt', 'ImageName', 'ks2-matlab-base')
```

- [Optional] Files generated by Matlab Compiler can be deleted:
  - In your terminal, go to the `kilosort_no_license` folder in this project:
  ```bash
  $ cd /path/to/spikeinterface-dockerfiles/kilosort_no_license
  ```
  - Run `rm` command:
  ```bash
  $ rm -r \
    includedSupportPackages.txt \
    ks2-matlab-basedocker/ \
    ks2_compiled \
    mccExcludedFiles.log \
    readme.txt \
    requiredMCRProducts.txt \
    run_ks2_compiled.sh \
    unresolvedSymbols.txt
  ```

## 4. Extending Base Image and creating final image

The Dockerfile in this folder applies some fixes and updates to the base image generated automatically by Matlab in order to properly run kilosort2:

- In your terminal, go to the folder for this project:
```bash
$ cd /path/to/spikeinterface-dockerfiles/kilosort_no_license/kilosort2-compiled
```

- Run build script:
```bash
$ source build.sh
```
