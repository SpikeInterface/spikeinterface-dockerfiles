#!/bin/bash
set -e

if [ $# == 0 ]; then
    echo "Usage: $0 param1 param2 param3 param4 param4"
    echo "* param1: spikeinterface path"
    echo "* param1: kilosort2 path"
    exit
fi

if [ $# -ne 2 ]; then
    echo "spikeinterface and kilosort2 path must be given"
    exit 1
fi


SPIKEINTERFACE_PATH=${1%/}
KILOSORT2_PATH=${2%/}


cd kilosort2-compiled
bash compile.sh $KILOSORT2_PATH $SPIKEINTERFACE_PATH
bash build.sh
cd ..