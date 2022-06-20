FROM python:3.8

# downgrade pip version to avoid dependency issues during installations
RUN pip install --no-input pip==21.2.4



# Install prerequisites
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# need to force some version
RUN pip install numpy==1.20
RUN pip install numba
RUN pip install git+https://github.com/scikit-learn-contrib/hdbscan.git


RUN pip install Cython
RUN pip install scipy pandas scikit-learn matplotlib seaborn tqdm openpyxl quantities neo
RUN pip install h5py
RUN pip install loky packaging

RUN pip install tridesclous==1.6.5
