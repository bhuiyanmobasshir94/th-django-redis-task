# th-django-redis-task

## Redis Server Installation

- sudo apt-get update
- sudo apt-get install redis-server

- sudo service redis-server start
- sudo service --status-all
- redis-cli
-- ping

- sudo systemctl status redis
- sudo systemctl start redis

## Setup conda environment

- conda create -n th_task python=3.6 pip
- conda activate th_task
- conda deactivate

## Loadtest

- sudo apt-get install npm
- sudo npm install -g loadtest
- loadtest -n 100 -k http://127.0.0.1:8000/values 

