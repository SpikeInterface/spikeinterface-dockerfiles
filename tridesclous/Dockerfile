FROM python:3.8

# downgrade pip version to avoid dependency issues during installations
RUN pip install --no-input pip==21.2.4

# Install prerequisites
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# need to force some version

# on 2022/01/12 : numba still force numpy<1.21 
RUN pip install numpy==1.20

RUN pip install numba

# on 2022/01/12 : hdbscan is not yet release
# see https://github.com/scikit-learn-contrib/hdbscan/issues/505
# so installation from source
RUN pip install git+https://github.com/scikit-learn-contrib/hdbscan.git


RUN pip install Cython
RUN pip install scipy pandas scikit-learn matplotlib seaborn tqdm openpyxl quantities neo
RUN pip install h5py
RUN pip install loky

RUN pip install tridesclous==1.6.4
