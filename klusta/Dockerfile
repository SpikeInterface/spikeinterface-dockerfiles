FROM python:3.7

RUN apt update && apt install -y build-essential 

# downgrade pip version to avoid dependency issues during installations
RUN pip install --no-input pip==21.2.4

RUN pip install numpy

# Install Klusta
RUN pip install Cython h5py tqdm six scipy
RUN pip install click klusta klustakwik2==0.2.7
