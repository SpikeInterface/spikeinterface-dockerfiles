FROM jupyter/datascience-notebook:hub-1.5.0

LABEL maintainer="Vincent Prevosto <prevosto@mit.edu>"

USER root
# APT packages
RUN apt update && \
    apt install -y --no-install-recommends \
    libgl1-mesa-glx \
    datalad && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# copy repo
WORKDIR /srv
RUN git clone https://github.com/SpikeInterface/spikeinterface.git

RUN fix-permissions $CONDA_DIR && \
fix-permissions /home/$NB_USER && \
fix-permissions /srv/spikeinterface

#Switch to user
USER $NB_UID

# update Anaconda and install pip 
RUN conda update -y conda && \
     conda install -y pip

# Conda installs
RUN conda config --set channel_priority flexible && \
    conda install -y -c conda-forge nb_conda_kernels \
    jupyter_contrib_nbextensions \
    jupyterlab-git \
    pynwb && \
    conda clean -tipsy

# Create environment
RUN ln -s /srv/spikeinterface /home/$NB_USER/
WORKDIR /home/$NB_USER/spikeinterface/installation_tips/
RUN conda env create -f full_spikeinterface_environment_mac.yml

# Make kernels available
SHELL ["conda","run","-n","spikeinterface","/bin/bash","-c"]
RUN conda install --quiet --yes ipykernel && \
    conda install --quiet --yes -c conda-forge datalad && \
    python -m ipykernel install --user --name spikeinterface --display-name "spikeinterface" && \
    pip install jupytext dotenv

# Configure git (required by datalad)
WORKDIR /home/$NB_USER/spikeinterface/
RUN git config --global --add user.name "Jovyan" && \
    git config --global --add user.email jovyan@example.net

# Create "getting started" notebook in home directory
WORKDIR /home/$NB_USER/spikeinterface/examples/getting_started/
RUN jupytext --to notebook plot_getting_started.py && \
    cp ~/spikeinterface/examples/getting_started/plot_getting_started.ipynb ~/getting_started.ipynb

# Make sure to switch back to user (avoid running ui containers as root)
USER $NB_UID
WORKDIR /home/$NB_USER
