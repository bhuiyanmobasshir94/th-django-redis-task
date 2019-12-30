# Django Caching Task

## Redis Server Installation
I have used ubuntu **16.04** on linux subsystem and followed the following commands to make this project environment.
<code>
  sudo apt-get update
  sudo apt-get install redis-server
<code>
To start and check the status of the redis server I have used following commands -
<code>
  sudo service redis-server start
  sudo service --status-all
<code>
Below commands are also used for starting and checking redis server but in my machine it didn't work.
<code>
  sudo systemctl start redis
  sudo systemctl status redis
<code>

## Setup conda environment
I love to use conda for my virtual environment and I made this in the following way - 
<code>
  conda create -n th_task python=3.6 pip
  conda activate th_task
<code>
To deactivate the environment - 
<code>
conda deactivate
<code>
Now go to my github repo main directory and run the following `run.sh` bash script. Assuming that you have activated you virtual env and your redis server is installed properly.
<code>
  bash run.sh
  bash test.sh
<code>
## Loadtest

You can also do some loadtesting on endpoints - 
<code>
  sudo apt-get install npm
  sudo npm install -g loadtest
  loadtest -n 100 -k http://127.0.0.1:8000/values 
<code>

