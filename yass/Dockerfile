#docker build -t ibl/yass:base .
FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

# link the cuda libraries
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

# setup time zone for tz
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV LANG C.UTF-8

RUN apt-get update
RUN apt-get install -y software-properties-common wget git

# Install conda from: https://towardsdatascience.com/conda-pip-and-docker-ftw-d64fe638dc45
SHELL [ "/bin/bash", "--login", "-c" ]

# Create a non-root user
ARG username=si
ARG uid=1000
ARG gid=100
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/$USER
RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid $UID \
    --gid $GID \
    --home $HOME \
    $USER

COPY entrypoint.sh /usr/local/bin/
RUN chown $UID:$GID /usr/local/bin/entrypoint.sh && \
    chmod u+x /usr/local/bin/entrypoint.sh


USER $USER
# install miniconda
ENV MINICONDA_VERSION 4.8.2
ENV CONDA_DIR $HOME/miniconda3
#https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh
ENV LATEST_CONDA_SCRIPT "Miniconda3-py37_$MINICONDA_VERSION-Linux-x86_64.sh"


RUN wget --quiet https://repo.anaconda.com/miniconda/$LATEST_CONDA_SCRIPT -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh

# make non-activate conda commands available
ENV PATH=$CONDA_DIR/bin:$PATH
# make conda activate command available from /bin/bash --login shells
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> ~/.profile
# make conda activate command available from /bin/bash --interative shells
RUN conda init bash

# create a project directory inside user home
ENV PROJECT_DIR $HOME/app
RUN mkdir $PROJECT_DIR
WORKDIR $PROJECT_DIR

ENV CONDA_ENV_NAME yass
RUN conda create -n $CONDA_ENV_NAME
RUN conda activate $CONDA_ENV_NAME 


# install yass
RUN conda install pytorch==1.2
#RUN git clone --depth 1 --branch v2.0 https://github.com/paninski-lab/yass \
RUN git clone https://github.com/paninski-lab/yass \
   && cd yass \
   && git checkout d9c9e2c52287afeb3256bdfde749f75f5083fd5d \
   && pip --no-cache-dir install -e . \
   && cd src/gpu_bspline_interp \
   && python setup.py install --force \
   && cd .. \
   && cd gpu_rowshift \
   && python setup.py install --force \
   && cd ../.. \
   && pip install .

RUN pip install scipy==1.2.0

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
