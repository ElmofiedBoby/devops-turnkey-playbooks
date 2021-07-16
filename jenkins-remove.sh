#!/bin/bash
ansible-playbook jenkins-uninstall.yml
echo "Waiting for 15s"
sleep 15s
ansible-playbook jenkins-remove-volumes.yml
