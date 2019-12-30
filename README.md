# Django Caching Task

## Redis Server Installation
I have used ubuntu **16.04** on linux subsystem and followed the following commands to make this project environment.
`
  sudo apt-get update
  sudo apt-get install redis-server
`
To start and check the status of the redis server I have used following commands -
`
  sudo service redis-server start
  sudo service --status-all
`
Below commands are also used for starting and checking redis server but in my machine it didn't work.
`
  sudo systemctl start redis
  sudo systemctl status redis
`

## Setup conda environment
I love to use conda for my virtual environment and I made this in the following way - 
`
  conda create -n th_task python=3.6 pip
  conda activate th_task
`
To deactivate the environment - 
`
conda deactivate
`
Now go to my github repo main directory and run the following `run.sh` bash script. Assuming that you have activated you virtual env and your redis server is installed properly.
`
  bash run.sh
  bash test.sh
`
## Loadtest

You can also do some loadtesting on endpoints - 
`
  sudo apt-get install npm
  sudo npm install -g loadtest
  loadtest -n 100 -k http://127.0.0.1:8000/values 
`

