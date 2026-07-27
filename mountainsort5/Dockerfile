FROM python:3.12

# downgrade pip version to avoid dependency issues during installations
RUN pip install --upgrade pip
RUN pip install "numpy<2.5"
RUN pip install mountainsort5==0.5.9
