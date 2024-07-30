FROM nvidia/cuda:11.7.1-base-ubuntu22.04

LABEL maintainer="Vincent Prevosto <prevosto@mit.edu>"

# USER root
# Ubuntu package installs
RUN apt update && \
    apt install -y --no-install-recommends \
    build-essential \
    libaio1 \
    opencl-headers \
    ocl-icd-libopencl1 \
    # nvidia-opencl-icd \ this is a virtual package - do not install. Instead install the actual package that matches your host's driver version
    libnvidia-compute-535 \
    clinfo \
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
ENV PYTHONPATH=$CONDA_DIR/bin:$CONDA_DIR/lib/python3.9/site-packages
RUN conda update conda && \
    conda install conda-build && \
    conda install conda-forge::ocl-icd-system
    # See pyopencl docs: 
    # https://documen.tician.de/pyopencl/misc.html#using-vendor-supplied-opencl-drivers-mainly-on-linux

# make conda activate command available from /bin/bash --login shells
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> /root/.profile 
# make conda activate command available from /bin/bash --interactive shells
RUN conda init bash

# Install IBL python port of pykilosort
RUN git clone https://github.com/njh27/spikesorting_fullpursuit.git /src/fullpursuit
WORKDIR /src/fullpursuit

# Install conda environment
SHELL ["conda","run","-n","base","/bin/bash","-c"]
RUN conda install -c intel mkl mkl-service
RUN conda install -c defaults numpy matplotlib
RUN conda install -c conda-forge pyopencl scipy scikit-learn
RUN pip install Cython 

# Install full binary pursuit
RUN conda install --quiet --yes -c defaults ipykernel && \
    python -m ipykernel install --user --display-name "fullpursuit" && \ 
    pip install -e .   

WORKDIR /