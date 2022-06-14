### Build this image
Build default image: 
docker build -t pykilosort:latest -f dockerfiles/Dockerfile .

Build image with additional testing components: 
docker build -t pykilosort:test -f dockerfiles/Dockerfile.testing context

### Run container
docker run --rm -it -v <host-data-folder>:<docker-data-folder> --gpus all pykilosort:latest
flags:
--rm: removes container once it's stopped
-it: for interactive session
-v: mounted volumes (directories)
--gpus: enables GPU use within container 

### Test
Download Neuropixel 1.0 data to your data directory: https://catalystneuro.github.io/spike-sorting-hackathon/datasets/datasets.html#allen-institute-example
(see also https://github.com/int-brain-lab/pykilosort/tree/ibl_prod/examples, although apparently not up to date)

$docker run --rm -it -v /my/dir/to/data:/data --gpus all pykilosort
#conda activate pyks2
#cd /data
    --- alternatively, get data from kachery (if installed and configured) ---
    ```
    wget https://catalystneuro.github.io/spike-sorting-hackathon/datasets/examples/example_allen_NP1.py
    python example_allen_NP1.py
    ```

The either run tests in ipython console, or run example from /home/test_file directory (if using `.testing` image), after editing directory paths
#ipython
```
from pathlib import Path
from pykilosort import run, add_default_handler, np1_probe, np2_probe

data_path = Path('/data/Allen_Institute_NP1/continuous_1min.bin')
dir_path = Path('/data/Allen_Institute_NP1/pyKS_output')
add_default_handler(level='INFO') # print output as the algorithm runs
run(data_path, dir_path=dir_path, probe=np1_probe(sync_channel=False))
```
