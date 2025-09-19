FROM python:3.12

# Install prerequisites
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# need to force some version
RUN pip install numpy
RUN pip install numba
RUN pip install hdbscan

RUN pip install Cython
RUN pip install scipy pandas scikit-learn matplotlib seaborn tqdm openpyxl quantities neo
RUN pip install h5py
RUN pip install loky packaging

RUN pip install tridesclous==1.6.9
