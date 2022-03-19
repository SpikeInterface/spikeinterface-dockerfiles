### How to build this image
Open a terminal, navigate to the spikeinterface directory, then run:   
`docker build -t spikeinterface:0.2 .`  
On Linux systems, you can also use the build script (after making it executable `chmod +x build.sh`):    
`./build.sh`  

### How to run the spikeinterface container
**Method 1**  
For Windows: drag and drop the data folder on `Run_SpikeInterface.bat`. Replace "mytoken" by  some other word.   
  
**Method 2**  
1. Open a terminal and navigate to the data directory. Then follow these instructions.  
2. Start the container  
*On Linux/MacOS*  
`export JUPYTER_TOKEN='mytoken'`
`docker run -d --rm --name spikeinterface -v "${PWD}":/home/jovyan/data -p 8888:8888 -e JUPYTER_TOKEN wanglabneuro/spikeinterface:0.1`  
*On Windows*  
`set JUPYTER_TOKEN=mytoken`
`docker run -d --rm --name spikeinterface -v "%CD%":/home/jovyan/data -p 8888:8888 -e JUPYTER_TOKEN wanglabneuro/spikeinterface:0.1`  
  
3. Then open http://localhost:8888/lab?token=mytoken in a browser.   

(Replace "mytoken" by some other word). 

**Important Note**  
The `--rm` flag means the container is a on-off (will self-destroy upon closure). 
To make the container persitant, remove the `--rm flag` from the docker call. In which case, the container will persist. To start a stopped container, run `docker start spikeinterface` in a terminal, or use the Docker Desktop interface to start it.  


  





