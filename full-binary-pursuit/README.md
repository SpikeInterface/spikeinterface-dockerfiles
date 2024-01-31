### Run container
docker run --rm -it -v <host-data-folder>:<docker-data-folder> --gpus all fullpursuit:latest
flags:
--rm: removes container once it's stopped
-it: for interactive session (-d for detached)
-v: mounted volumes (directories)
--gpus: enables GPU use within container 

### Build this image
Build default image: 
docker build -t fullpursuit-base:latest .

Note: Full binary pursuit relies on opencl. Installation varies by OS and CPU / GPU type. 
For Intel CPUs, see https://www.intel.com/content/www/us/en/developer/articles/tool/opencl-drivers.html. 
For configuration on Ubuntu and Docker, see also https://linuxhandbook.com/setup-opencl-linux-docker/.  On Ubuntu, you may need to add your user to the `video` and `render` groups to access the GPU. 
```
sudo gpasswd -a $USER render
sudo gpasswd -a $USER video
```
Then log out and back in to apply the changes: `su - $USER`

Check fullpursuit version:
docker run --rm -it wanglabneuro/fullpursuit-base:latest bash -c "python -c 'import spikesorting_fullpursuit; print(spikesorting_fullpursuit.__version__)'"

Check that pyopencl can detect your graphics card:
docker run --rm -it --gpus all  wanglabneuro/fullpursuit-base:latest bash -c "python -c 'import pyopencl as cl; platforms = cl.get_platforms(); print(platforms[0].get_devices(cl.device_type.GPU))'"

### Test
Adapted from the readme file's instructions.

First make the voltage data and save ground truth (mounting the host data folder to the docker data folder):  
```bash
docker run --rm -it -v <host-data-folder>:<docker-data-folder> --gpus all wanglabneuro/fullpursuit-base:latest bash -c "python /src/fullpursuit/demos/make_and_save_voltage.py <docker-data-folder>/test_voltage.npy <docker-data-folder>/test_ground_truth.pickle"
```
e.g.:  
Create the data folder: `mkdir -p /home/$USER/data/fullpursuit_data`
Then create the groundtruth data: `docker run --rm -it -v /home/$USER/data/fullpursuit_data:/data --gpus all wanglabneuro/fullpursuit-base:latest bash -c "python /src/fullpursuit/demos/make_and_save_voltage.py /data/test_voltage.npy /data/test_ground_truth.pickle"`

Then run the sorting algorithm on the generated synthetic data:  
```bash
docker run --rm -it -v <host-data-folder>:<docker-data-folder> --gpus all wanglabneuro/fullpursuit-base:latest bash -c "python /src/fullpursuit/demos/test_demo_run_sort.py <docker-data-folder>/test_voltage.npy <docker-data-folder>/sorted_demo.pickle"
```
e.g.:  
`docker run --rm -it -v /home/$USER/data/fullpursuit_data:/data --gpus all wanglabneuro/fullpursuit-base:latest bash -c "python /src/fullpursuit/demos/test_demo_run_sort.py /data/test_voltage.npy /data/sorted_demo.pickle"`

Run automated postprocessing to place sorter output into a dictionary sorted neurons:  
```bash
docker run --rm -it -v <host-data-folder>:<docker-data-folder> --gpus all wanglabneuro/fullpursuit-base:latest bash -c "python /src/fullpursuit/demos/test_demo_postprocessing.py <docker-data-folder>/sorted_demo.pickle <docker-data-folder>/sorted_neurons.pickle"
```
e.g.:  
`docker run --rm -it -v /home/$USER/data/fullpursuit_data:/data --gpus all wanglabneuro/fullpursuit-base:latest bash -c "python /src/fullpursuit/demos/test_demo_postprocessing.py /data/sorted_demo.pickle /data/sorted_neurons.pickle"`

Finally run a quick script that compares sorted results to the ground truth generated data and make a couple figures:  
```bash
docker run --rm -it -v <host-data-folder>:<docker-data-folder> --gpus all wanglabneuro/fullpursuit-base:latest bash -c "python /src/fullpursuit/demos/test_demo_results.py <docker-data-folder>/sorted_neurons.pickle <docker-data-folder>/test_ground_truth.pickle"
```
e.g.:  
`docker run --rm -it -v /home/$USER/data/fullpursuit_data:/data --gpus all wanglabneuro/fullpursuit-base:latest bash -c "python /src/fullpursuit/demos/test_demo_results.py /data/sorted_neurons.pickle /data/test_ground_truth.pickle"`
