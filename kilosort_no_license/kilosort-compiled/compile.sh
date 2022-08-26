#!/bin/bash

if [ $# == 0 ]; then
    echo "Usage: $0 param1 param2"
    echo "* param1: KiloSort path"
    echo "* param2: spikeinterface path"
    exit
fi

if [ $# -ne 2 ]; then
    echo "spikeinterface and kilosort path must be given"
    exit 1
fi

ROOT_PATH=$(pwd)
echo "Creating tmp folder in: ${ROOT_PATH}"
mkdir -p tmp
TMP_DIR=$ROOT_PATH/tmp
KS_PATH=$1
SI_PATH=$2
echo "Kilosort path: ${KS_PATH}"
echo "spike-interface path: ${SI_PATH}"

echo "Compiling CUDA files"
cd ${KS_PATH}/CUDA
matlab -batch "mexGPUall"

cd $TMP_DIR

echo "Compiling kilosort_master from spikeinterface repository..."
matlab -batch "mcc -m ${SI_PATH}/spikeinterface/sorters/kilosort/kilosort_master.m -a ${SI_PATH}/spikeinterface/sorters/utils -a ${KS_PATH}"

echo "Creating base docker image..."
matlab -batch "compiler.package.docker('kilosort_master', 'requiredMCRProducts.txt', 'ImageName', 'ks-matlab-base')"

cd $ROOT_PATH
rm -r $TMP_DIR
