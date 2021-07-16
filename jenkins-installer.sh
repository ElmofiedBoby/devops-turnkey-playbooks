#!/bin/bash
ansible-playbook jenkins-install.yml
echo "5s wait"
sleep 5s
ansible-playbook jenkins-ssh.yml
echo "5s wait"
sleep 5s
ansible-playbook git-configure.yml
echo "15s wait"
sleep 15s
ansible-playbook jenkins-configure.yml
