#!/bin/bash

# docker build -t spikeinterface/pykilosort-base:latest -t spikeinterface/pykilosort-base:ibl-1.3 .
# docker build -t wanglabneuro/pykilosort-base:latest -t wanglabneuro/pykilosort-base:ibl-1.3 .
# docker build -t wanglabneuro/pykilosort-base:latest -t wanglabneuro/pykilosort-base:ibl-1.4.7_cuda-11.3.1 .
docker build -t wanglabneuro/pykilosort-base:latest -t wanglabneuro/pykilosort-base:ibl-1.4.7_cuda-11.5.2 .

# version info
# 01/21/2024 - IBL 1.4.7 CUDA 11.3.1 Ubuntu 20.04
# 02/01/2024 - IBL 1.4.7 CUDA 11.5.2 Ubuntu 20.04
