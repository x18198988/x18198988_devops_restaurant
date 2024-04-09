#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/restaurant/requirements.txt
sudo chmod 777 /home/ubuntu/restaurant
sudo chmod 777 /home/ubuntu/restaurant/db.sqlite3
