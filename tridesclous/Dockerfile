FROM python:3.8

RUN pip install --upgrade pip

# on 2022/01/12 : numba still force <1.21 
RUN pip install numpy==1.20

# on 2022/01/12 : hdbscan is not yet release
# see https://github.com/scikit-learn-contrib/hdbscan/issues/505
# so installation from source
RUN pip install git+https://github.com/scikit-learn-contrib/hdbscan.git

# Install prerequisites
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install Cython
RUN pip install scipy numpy pandas scikit-learn matplotlib seaborn tqdm openpyxl quantities neo numba hdbscan
RUN pip install h5py
RUN pip install loky

RUN pip install tridesclous==1.6.4
