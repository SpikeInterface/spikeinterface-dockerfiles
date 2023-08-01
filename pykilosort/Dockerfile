FROM nvidia/cuda:11.0.3-base-ubuntu18.04

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
ENV MINICONDA_VERSION 23.3.1-0
ENV PY_VERSION py39
ENV CONDA_DIR /home/miniconda3
ENV LATEST_CONDA_SCRIPT "Miniconda3-${PY_VERSION}_${MINICONDA_VERSION}-Linux-x86_64.sh"

RUN wget --quiet https://repo.anaconda.com/miniconda/$LATEST_CONDA_SCRIPT -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh
ENV PATH=$CONDA_DIR/bin:$PATH
RUN conda update conda && \
    conda install conda-build

# make conda activate command available from /bin/bash --login shells
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> /root/.profile 
# make conda activate command available from /bin/bash --interactive shells
RUN conda init bash

# Install IBL python port of pykilosort - using #16 PR to remove prints from cupy
RUN git clone -b remove_prints https://github.com/alejoe91/pykilosort.git /src/pykilosort
WORKDIR /src/pykilosort

# modify env file so that env extends on base
RUN sed -i "s/pyks2/base/" pyks2.yml
RUN sed -i "s/- spikeinterface//" pyks2.yml

# Create environment
RUN conda env update --name base --file pyks2.yml --prune

# Install pykilosort
RUN conda install --quiet --yes ipykernel && \
    python -m ipykernel install --user --display-name "pyKilosort" && \ 
    conda develop .   

#--name pyks2
WORKDIR /
