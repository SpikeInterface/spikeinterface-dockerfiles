FROM nvidia/cuda:10.0-base-ubuntu18.04 

LABEL maintainer="Vincent Prevosto <prevosto@mit.edu>"

# USER root
# # Ubuntu package installs
RUN apt update 
RUN apt install -y --no-install-recommends \
    libfftw3-dev \
    git \
    wget && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# install miniconda
ENV MINICONDA_VERSION 4.12.0
ENV CONDA_DIR /home/miniconda3
ENV LATEST_CONDA_SCRIPT "Miniconda3-py38_$MINICONDA_VERSION-Linux-x86_64.sh"

RUN wget --quiet https://repo.anaconda.com/miniconda/$LATEST_CONDA_SCRIPT -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh
# RUN echo 'export PATH="~/miniconda/bin:$PATH"' >> ~/.bashrc 
ENV PATH=$CONDA_DIR/bin:$PATH
RUN conda update conda && \
    conda install conda-build

# Install IBL port of pykilosort
RUN git clone -b drift_test_stable https://github.com/kushbanga/pykilosort.git /src/pykilosort
WORKDIR /src/pykilosort

# Create environment
RUN conda env create -f pyks2.yml

# Install pykilosort
SHELL ["conda","run","-n","pyks2","/bin/bash","-c"]
# RUN conda install --quiet --yes ipykernel && \
#     python -m ipykernel install --user --name pyks2 --display-name "pyKilosort" && \
RUN conda develop .




