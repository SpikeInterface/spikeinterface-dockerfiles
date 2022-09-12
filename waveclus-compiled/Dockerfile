FROM waveclus-matlab-base

COPY --from=waveclus-snippets-matlab-base /usr/bin/mlrtapp/waveclus_snippets_compiled /usr/bin/mlrtapp/waveclus_snippets_compiled
RUN chmod 755 /usr/bin/mlrtapp/waveclus_compiled
RUN chmod 755 /usr/bin/mlrtapp/waveclus_snippets_compiled
ENV PATH="/usr/bin/mlrtapp:${PATH}"

# Installing Python with miniconda
RUN apt-get update && \
    apt-get install -y build-essential  && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV MINICONDA_VERSION 4.8.2
ENV CONDA_DIR /home/miniconda3
ENV LATEST_CONDA_SCRIPT "Miniconda3-py38_$MINICONDA_VERSION-Linux-x86_64.sh"

RUN wget --quiet https://repo.anaconda.com/miniconda/$LATEST_CONDA_SCRIPT -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh
ENV PATH=$CONDA_DIR/bin:$PATH

RUN pip install hdf5storage
