#!/bin/bash
ansible-playbook git-install.yml
echo "wait 15s"
sleep 15s
ansible-playbook git-configure.yml
echo "wait 15s"
sleep 15s
ansible-playbook git-create-repository.yml
