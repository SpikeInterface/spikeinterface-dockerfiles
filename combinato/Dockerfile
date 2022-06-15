FROM python:3.8

LABEL maintainer="Vincent Prevosto <prevosto@mit.edu>"

# Ubuntu package installs
RUN apt update && \
    apt install -y --no-install-recommends \
    git && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install \
    numpy \
    scipy \
    matplotlib \
    PyWavelets \
    tables \
    pyqt5 \
    ipython

# Clone Combinato
WORKDIR /src
RUN git clone https://github.com/jniediek/combinato.git

# Add Combinato repository to paths
ENV COMBINATO_DIR /src/combinato
ENV PATH=$PATH:$COMBINATO_DIR
ENV PYTHONPATH=$PYTHONPATH:/usr/local/bin/python3:$COMBINATO_DIR
RUN echo $' \n\
    PATH=$PATH:/src/combinato \n\
    PYTHONPATH=$PYTHONPATH:/usr/local/bin/python3:$COMBINATO_DIR \n\
    export PATH PYTHONPATH  ' >> /root/.bashrc

# Install Combinato
WORKDIR /src/combinato
RUN python3 setup_options.py


