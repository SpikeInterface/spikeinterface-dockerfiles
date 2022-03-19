### How to build this image
Open a terminal, navigate to the spikeinterface directory, then run:   
`docker build -t wanglabneuro/spikeinterface:0.2 .`  
On Linux systems, you can also use the build script (after making it executable `chmod +x build.sh`):    
`./build.sh`  

### How to run the spikeinterface container
**Method 1**  
For Windows: drag and drop the data folder on `Run_SpikeInterface.bat`. Replace "mytoken" by whatever word.   
  
**Method 2**  
On Linux/MacOS:  
`export JUPYTER_TOKEN='mytoken'`
`docker run -d --rm --name spikeinterface -v "${PWD}":/home/jovyan/work -p 8888:8888 -e JUPYTER_TOKEN wanglabneuro/spikeinterface:0.1`  

On Windows:  
`set JUPYTER_TOKEN=mytoken`
`docker run -d --rm --name spikeinterface -v "%CD%":/home/jovyan/work -p 8888:8888 -e JUPYTER_TOKEN wanglabneuro/spikeinterface:0.1`  
  
Then open http://localhost:8888/lab?token=mytoken in a browser.




