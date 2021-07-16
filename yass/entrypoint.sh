#!/bin/bash --login
set -e
conda activate $CONDA_ENV_NAME 
exec "$@"
