#!/bin/bash

# usually the tag would be the version of the sorter
# but in this case since 3 is already in the name, maybe the tag should be 0.1.x
docker build -t spikeinterface/kilosort3-base:0.1.0 .