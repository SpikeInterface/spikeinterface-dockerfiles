FROM nvidia/cuda:12.0.0-base-ubuntu20.04

LABEL maintainer="Alessio Buccino <alessiop.buccino@gmail.com>"

# USER root
# Ubuntu package installs
RUN apt update && \
    apt install -y --no-install-recommends \
    libfftw3-dev \
    git \
    wget && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# install miniconda
ENV MINICONDA_VERSION=25.5.1-0
ENV PYTHON_VERSION=py312
ENV CONDA_DIR=/home/miniconda3
ENV LATEST_CONDA_SCRIPT="Miniconda3-${PYTHON_VERSION}_${MINICONDA_VERSION}-Linux-x86_64.sh"
    
RUN wget --quiet https://repo.anaconda.com/miniconda/$LATEST_CONDA_SCRIPT -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh
ENV PATH=$CONDA_DIR/bin:$PATH
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
    conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r && \
    conda update conda && \
    conda install conda-build

# make conda activate command available from /bin/bash --login shells
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> /root/.profile 
# make conda activate command available from /bin/bash --interactive shells
RUN conda init bash

# install torch
RUN pip install torch torch-tensorrt tensorrt

# install rt-sort
RUN pip install git+https://github.com/braingeneers/braindance#egg=braindance[rt-sort]
