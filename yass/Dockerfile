#docker build -t ibl/yass:base .
FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

# link the cuda libraries
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

# setup time zone for tz
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install python3.7
RUN apt-get update
RUN apt-get install -y software-properties-common wget
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.7 python3.7-dev python3.7-tk python3-pip python3.7-venv git ffmpeg libgtk-3-dev

# Install Python dependencies
ARG PYTHON=python3.7
ENV LANG C.UTF-8
ENV CONDA_PATH=/opt/anaconda3
ENV ENVIRONMENT_NAME=main
SHELL ["/bin/bash", "-c"]

# Download and install Anaconda.
ENV LATEST_CONDA_SCRIPT "Anaconda3-5.3.1-Linux-x86_64.sh"
ENV PATH="/root/anaconda2/bin:${PATH}"

RUN wget https://repo.continuum.io/archive/$LATEST_CONDA_SCRIPT

RUN bash $LATEST_CONDA_SCRIPT -b -p /home/anaconda3 \
	&& echo "export PATH=/home/anaconda/bin:$PATH" >> ~/.bashrc \
	&& /bin/bash -c "source /root/.bashrc"

ENV PATH /home/anaconda3/bin:$PATH

RUN conda install pytorch==1.2
#RUN rm $LATEST_CONDA_SCRIPT
#conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch

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

RUN pip install scipy==1.2.0
#cd yass/samples/10chan
#yass sort config.yaml
