FROM python:3.8

# downgrade pip version to avoid dependency issues during installations
RUN pip install --no-input pip==21.2.4

RUN pip install numpy

# Install prerequisites
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install Cython
RUN pip install scipy numpy pandas scikit-learn matplotlib seaborn tqdm openpyxl quantities neo numba hdbscan
RUN pip install h5py
RUN pip install loky

RUN pip install tridesclous==1.6.4
