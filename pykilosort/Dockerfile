FROM nvidia/cuda:10.0-base-ubuntu18.04 

LABEL maintainer="Vincent Prevosto <prevosto@mit.edu>"

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
ENV MINICONDA_VERSION 4.12.0
ENV CONDA_DIR /home/miniconda3
ENV LATEST_CONDA_SCRIPT "Miniconda3-py38_$MINICONDA_VERSION-Linux-x86_64.sh"

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

# Install python port of pykilosort
RUN git clone https://github.com/int-brain-lab/pykilosort.git /src/pykilosort
WORKDIR /src/pykilosort
# Switch to MouseLand/develop branch - may revert to kushbanga/drift_test_stable in the future
# RUN git remote add MouseLand https://github.com/MouseLand/pykilosort.git && \
#     git fetch MouseLand && git checkout MouseLand/develop && git checkout -b develop

# modify env file so that env extends on base
RUN sed -i "s/pyks2/base/" pyks2.yml
RUN sed -i "s/- spikeinterface//" pyks2.yml
RUN cat pyks2.yml

# Create environment
RUN conda env update --name base --file pyks2.yml --prune

# Install pykilosort
RUN conda install --quiet --yes ipykernel && \
    python -m ipykernel install --user --display-name "pyKilosort" && \ 
    conda develop .   

# install phylib from master because of read-only bug (https://github.com/cortex-lab/phylib/pull/35)
RUN pip uninstall -y phylib && pip install git+https://github.com/cortex-lab/phylib.git

#--name pyks2
WORKDIR /
