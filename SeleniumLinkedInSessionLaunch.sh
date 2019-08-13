#!/usr/bin/env bash
nohup python -u launchSeleniumInstance.py 1> /tmp/selInst.txt &
echo $! > .pid
