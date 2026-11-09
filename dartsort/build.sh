#!/bin/bash

# Extract the KILOSORT4_VERSION from the Dockerfile
DARTSORT_VERSION=$(grep -E '^ENV DARTSORT_VERSION=' "Dockerfile" | awk -F= '{print $2}' | tr -d '[:space:]')
CUDA_VERSION=$(grep -E '^ENV CUDA_VERSION=' "Dockerfile" | awk -F= '{print $2}' | tr -d '[:space:]')
echo "Building dartsort:$DARTSORT_VERSION"

docker build -t spikeinterface/dartsort-base:latest -t spikeinterface/dartsort-base:${DARTSORT_VERSION}_cuda-${CUDA_VERSION} .
