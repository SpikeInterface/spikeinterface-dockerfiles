#!/bin/bash

# usually the tag would be the version of the sorter
# but in this case since 2 is already in the name, maybe the tag should be 0.1.x
docker build -t spikeinterface/kilosort2-si-0.12:0.1.0 .