#!/bin/bash
set -e

if [ $# == 0 ]; then
    echo "Usage: $0 param1 param2"
    echo "* param1: waveclus path"
    echo "* param2: spikeinterface path"
    exit
fi

if [ $# -ne 2 ]; then
    echo "spikeinterface and waveclus path must be given"
    exit 1
fi

WC_COMPILED_NAME="waveclus_compiled"
WC_SNIPPETS_COMPILED_NAME="waveclus_snippets_compiled"
WC_PATH=${1%/}
SI_PATH=${2%/}
WORK_DIR=$(pwd)
SOURCE_DIR=$( dirname -- "$0"; )
TMP_DIR=$SOURCE_DIR/tmp

echo "waveclus path: ${WC_PATH}"
echo "spike-interface path: ${SI_PATH}"

echo "Creating tmp folder: $TMP_DIR"
cd $WORK_DIR
mkdir -p $TMP_DIR

echo "Compiling waveclus..."
cd $TMP_DIR
EXTERNAL_SORTERS_FOLDER=${SI_PATH}/src/spikeinterface/sorters/external/
matlab -batch "mcc -m ${EXTERNAL_SORTERS_FOLDER}/waveclus_master.m -a ${SI_PATH}/src/spikeinterface/sorters/utils -a ${WC_PATH} -o ${WC_COMPILED_NAME}"

echo "Creating base docker image..."
matlab -batch "compiler.package.docker('${WC_COMPILED_NAME}', 'requiredMCRProducts.txt', 'ImageName', 'waveclus-matlab-base')"

echo "Compiling waveclus_snippets..."
matlab -batch "mcc -m ${EXTERNAL_SORTERS_FOLDER}/waveclus_snippets_master.m -a ${SI_PATH}/src/spikeinterface/sorters/utils -a ${WC_PATH} -o ${WC_SNIPPETS_COMPILED_NAME}"

echo "Creating base docker image..."
matlab -batch "compiler.package.docker('${WC_SNIPPETS_COMPILED_NAME}', 'requiredMCRProducts.txt', 'ImageName', 'waveclus-snippets-matlab-base')"


cd $WORK_DIR
rm -r $TMP_DIR
