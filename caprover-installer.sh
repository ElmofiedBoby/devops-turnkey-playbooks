#!/bin/bash
ansible-playbook docker-install.yml
echo "wait 10s"
sleep 10s
ansible-playbook caprover-install.yml
echo "wait 10s"
sleep 10s
ansible-playbook caprover-config.yml
