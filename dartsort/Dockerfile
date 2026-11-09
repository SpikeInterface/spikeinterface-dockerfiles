FROM nvidia/cuda:12.9.2-cudnn-runtime-ubuntu24.04

LABEL maintainer="Alessio Buccino <alessiop.buccino@gmail.com>"

ENV DARTSORT_VERSION=0.5.32
ENV CUDA_VERSION=12.9.2

# Ubuntu 24.04 marks system Python as externally managed (PEP 668); fine to override in a container.
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# Install Python 3, Pip, and clean up apt caches to save space
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python-is-python3 \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install tbb==2021.13.1
# CUDA 12.9 wheels (matches the base image); the default PyPI torch is CUDA 13, which has no kernels for Volta and older GPUs
RUN pip install torch==2.13.0 torchaudio==2.11.0 torchvision==0.28.0 --index-url https://download.pytorch.org/whl/cu129
RUN pip install dartsort==$DARTSORT_VERSION