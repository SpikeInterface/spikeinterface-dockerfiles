#!/bin/bash
set -e

if [ $# == 0 ]; then
    echo "Usage: $0 param1 param2"
    echo "* param1: hdsort path"
    echo "* param2: spikeinterface path"
    exit
fi

if [ $# -ne 2 ]; then
    echo "spikeinterface and hdsort path must be given"
    exit 1
fi

HDSORT_COMPILED_NAME="hdsort_compiled"
HDSORT_PATH=${1%/}
SI_PATH=${2%/}
WORK_DIR=$(pwd)
SOURCE_DIR=$( dirname -- "$0"; )
TMP_DIR=$SOURCE_DIR/tmp

echo "hdsort path: ${HDSORT_PATH}"
echo "spike-interface path: ${SI_PATH}"

echo "Creating tmp folder: $TMP_DIR"
cd $WORK_DIR
mkdir -p $TMP_DIR

echo "Compiling hdsort..."
cd $TMP_DIR
matlab -batch "mcc -m ${SI_PATH}/spikeinterface/sorters/hdsort/hdsort_master.m -a ${SI_PATH}/spikeinterface/sorters/utils -a ${HDSORT_PATH} -o ${HDSORT_COMPILED_NAME}"

echo "Creating base docker image..."
matlab -batch "compiler.package.docker('${HDSORT_COMPILED_NAME}', 'requiredMCRProducts.txt', 'ImageName', 'hdsort-matlab-base')"

cd $WORK_DIR
rm -r $TMP_DIR
