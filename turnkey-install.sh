#!/bin/bash
bash sshagentscript.sh
sleep 5s
bash caprover-installer.sh
sleep 5s
bash git-installer.sh
sleep 5s
bash jenkins-installer.sh
sleep 5s
bash tomcat-installer.sh
sleep 5s
