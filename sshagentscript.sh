#!/bin/bash
chmod 600 ~/.ssh/niniryju
eval `ssh-agent`
ssh-add ~/.ssh/niniryju
