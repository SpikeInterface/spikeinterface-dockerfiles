#!/bin/bash

# Extract the KILOSORT4_VERSION from the Dockerfile
KILOSORT4_VERSION=$(grep -E '^ENV KILOSORT4_VERSION=' "Dockerfile" | awk -F= '{print $2}' | tr -d '[:space:]')
echo "Building kilosort4-base:$KILOSORT4_VERSION"

docker build -t spikeinterface/kilosort4-base:latest -t spikeinterface/kilosort4-base:${KILOSORT4_VERSION}_cuda-12.0.0 .
