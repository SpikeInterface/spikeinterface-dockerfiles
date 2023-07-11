#!/bin/bash
set -e

if [ $# == 0 ]; then
    echo "Usage: $0 param1 param2 param3 param4 param4"
    echo "* param1: spikeinterface path"
    echo "* param1: kilosort1 path"
    echo "* param1: kilosort2 path"
    echo "* param1: kilosort2.5 path"
    echo "* param1: kilosort3 path"
    exit
fi

if [ $# -ne 5 ]; then
    echo "spikeinterface and kilosort paths (1, 2, 2.5, 3) must be given"
    exit 1
fi


SPIKEINTERFACE_PATH=${1%/}
KILOSORT_PATH=${2%/}
KILOSORT2_PATH=${3%/}
KILOSORT25_PATH=${4%/}
KILOSORT3_PATH=${5%/}


cd kilosort-compiled
bash compile.sh $KILOSORT_PATH $SPIKEINTERFACE_PATH
bash build.sh
cd ..

cd kilosort2-compiled
bash compile.sh $KILOSORT2_PATH $SPIKEINTERFACE_PATH
bash build.sh
cd ..

cd kilosort2_5-compiled
bash compile.sh $KILOSORT25_PATH $SPIKEINTERFACE_PATH
bash build.sh
cd ..

cd kilosort3-compiled
bash compile.sh $KILOSORT3_PATH $SPIKEINTERFACE_PATH
bash build.sh
cd ..