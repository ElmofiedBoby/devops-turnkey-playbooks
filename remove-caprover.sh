#!/bin/bash
sudo docker rm -vf $(sudo docker ps -a -q)
sudo docker rmi -f $(sudo docker images -a -q)
sudo docker service rm $(sudo docker service ls -q)
sudo docker swarm leave --force
sudo docker system prune -a -y
sudo rm -rf /captain
sudo docker rm -vf $(sudo docker ps -a -q)
sudo docker rmi -f $(sudo docker images -a -q)
