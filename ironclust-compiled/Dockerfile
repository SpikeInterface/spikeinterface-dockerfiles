FROM ironclust-base

ENV PATH="/usr/bin/mlrtapp:${PATH}"

RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get install git python3.8 python3.8-dev -y
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
RUN apt-get install python3-pip -y
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
RUN pip install -U pip

