FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

# link the cuda libraries
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

#########################################
### Python
RUN apt update && apt -y install git wget build-essential
RUN apt install -y python3 python3-pip
RUN rm -f /usr/bin/python && ln -s python3 /usr/bin/python
RUN rm -f /usr/bin/pip && ln -s pip3 /usr/bin/pip
RUN DEBIAN_FRONTEND=noninteractive apt install -y python3-tk

RUN pip install numpy

# gcc-8 (cuda mex doesn't seem to work with gcc >8)
RUN apt-get install -y gcc-8 g++-8 && ln -sf /usr/bin/gcc-8 /usr/bin/gcc && ln -sf /usr/bin/g++-8 /usr/bin/g++

# Clone the source code for kilosort2
RUN git clone https://github.com/MouseLand/pykilosort.git && cd pykilosort \
  && pip install -r requirements.txt && python setup.py install
