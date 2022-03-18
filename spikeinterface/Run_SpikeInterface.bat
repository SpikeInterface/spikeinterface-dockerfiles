@echo off
Title Drag and drop a data folder
Mode con cols=60 lines=3
IF [%1] EQU [] Goto:Error
set JUPYTER_TOKEN=mytoken
docker run -d --rm --name spikeinterface -v "%~1":/home/jovyan/data -p 8888:8888 -e JUPYTER_TOKEN wanglabneuro/spikeinterface:0.1
TIMEOUT /T 2
START /W "" http://localhost:8888/lab?token=mytoken
ECHO Spike Interface started
TIMEOUT /T 2
Exit /b

::**********************************************************
:Error
Color 0C & echo(
ECHO    You must drag and drop a folder on this batch program 
Timeout /T 5 /NoBreak >nul
Exit /b
::**********************************************************