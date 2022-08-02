FROM python:3.8

# downgrade pip version to avoid dependency issues during installations
RUN pip install --no-input pip==21.2.4

RUN pip install numpy

RUN pip install requests
# Install MountainSort4
RUN pip install mountainsort4==1.0.3
