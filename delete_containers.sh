#!bin/bash

sudo docker rm -f $(sudo docker ps --format "{{.ID}}")