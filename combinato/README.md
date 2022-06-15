### Build this image
Build default image: 
docker build -t combinato:latest .

### Run container in bash
docker run --rm -it -v <host-data-folder>:<docker-data-folder> spikeinterface/combinato /bin/sh
flags:
--rm: removes container once it's stopped
-it: for interactive session
-v: mounted volumes (directories)

### Test
python3 tools/test_installation.py
