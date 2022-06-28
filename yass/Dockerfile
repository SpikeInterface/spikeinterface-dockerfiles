FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

# link the cuda libraries
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

# fix nvidia gpg
RUN rm -f /etc/apt/sources.list.d/cuda.list
RUN rm -f /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-key del 7fa2af80
RUN apt-get update && apt-get install -y --no-install-recommends wget
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb
RUN dpkg -i cuda-keyring_1.0-1_all.deb

# install ubuntu packages
RUN apt-get update
RUN apt-get install -y git software-properties-common
 
# set shell to /bin/bash for compatibility with conda
# (hints from: https://towardsdatascience.com/conda-pip-and-docker-ftw-d64fe638dc45)
SHELL [ "/bin/bash", "--login",  "-c" ]

# install miniconda
ENV MINICONDA_VERSION 4.8.2
ENV CONDA_DIR /home/miniconda3
ENV LATEST_CONDA_SCRIPT "Miniconda3-py37_$MINICONDA_VERSION-Linux-x86_64.sh"

RUN wget --quiet https://repo.anaconda.com/miniconda/$LATEST_CONDA_SCRIPT -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh

# make non-activate conda commands available
ENV PATH=$CONDA_DIR/bin:$PATH
# make conda activate command available from /bin/bash --login shells
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> /root/.profile 
# make conda activate command available from /bin/bash --interactive shells
RUN conda init bash

# install YASS
RUN conda install pytorch==1.2
RUN git clone https://github.com/paninski-lab/yass \
   && cd yass \
   && pip --no-cache-dir install -e . \
   && cd src/gpu_bspline_interp \
   && python setup.py install --force \
   && cd .. \
   && cd gpu_rowshift \
   && python setup.py install --force \
   && cd ../.. \
   && pip install .

# fix versions of scipy and pyyaml (to avoid Loader problem)
RUN pip install scipy==1.7.3 && pip install pyyaml==5.3

