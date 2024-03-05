FROM nvidia/cuda:11.5.2-base-ubuntu20.04

LABEL maintainer="Alessio Buccino <alessiop.buccino@gmail.com>"

# USER root
# Ubuntu package installs
RUN apt update && \
    apt install -y --no-install-recommends \
    libfftw3-dev \
    nano \
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

# Install IBL python port of pykilosort
RUN git clone -b 1.4.7 https://github.com/int-brain-lab/pykilosort.git /src/pykilosort
WORKDIR /src/pykilosort

# modify env file so that env extends on base
RUN sed -i "s/pyks2/base/" pyks2.yml
# edit the python line to keep the current python version (e.g., 3.9), otherwise it may upgrade (e.g., to 3.10.x), conflict with numba and break the installation.
RUN PYTHON_VERSION=$(python --version | cut -d ' ' -f 2) && \
    sed -i "s/- python.*/- python=$PYTHON_VERSION/" pyks2.yml
# remove the spikeinterface dependency
RUN sed -i "s/- spikeinterface//" pyks2.yml

# Create environment
RUN conda env update --name base --file pyks2.yml --prune

# Install pykilosort
RUN conda install --quiet --yes ipykernel && \
    python -m ipykernel install --user --display-name "pyKilosort" && \ 
    pip install -e .
RUN conda clean --all --yes

WORKDIR /
