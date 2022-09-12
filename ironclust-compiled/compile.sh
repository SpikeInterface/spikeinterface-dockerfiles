#!/bin/bash
set -e

if [ $# == 0 ]; then
    echo "Usage: $0 param1"
    echo "* param1: Ironclust path"
fi

if [ $# -ne 1 ]; then
    echo "ironclust path must be given"
    exit 1
fi

IC_COMPILED_NAME="p_ironclust"
IC_PATH=${1%/}/matlab
WORK_DIR=$(pwd)
SOURCE_DIR=$( dirname -- "$0"; )
TMP_DIR=$SOURCE_DIR/tmp

echo "Ironclust path: ${IC_PATH}"

echo "Compiling CUDA files"
cd $IC_PATH
matlab -batch "irc2 compile"

echo "Creating tmp folder: ${TMP_DIR}"
cd $WORK_DIR
mkdir -p $TMP_DIR

echo "Compiling p_ironclust..."
cd $TMP_DIR

# Generating multiple "-a filename" string
# This is needed because wildcard pattern /* doesn't work
# properly when running mcc outside matlab's console
ADD_FILES=""
for fname in $(eval "ls ${IC_PATH} -I \"*.pdf\" -p | grep -v /"); do
    ADD_FILES="${ADD_FILES} -a ${IC_PATH}/${fname}"
done
ADD_FILES="${ADD_FILES} -a ${IC_PATH}/prb"
ADD_FILES="${ADD_FILES} -a ${IC_PATH}/prb_json"

matlab -batch "mcc -m ${IC_PATH}/p_ironclust.m ${ADD_FILES} -o ${IC_COMPILED_NAME}"

echo "Creating base docker image..."
matlab -batch "compiler.package.docker('${IC_COMPILED_NAME}', 'requiredMCRProducts.txt', 'ImageName', 'ironclust-matlab-base')"

cd $WORK_DIR
rm -r $TMP_DIR
