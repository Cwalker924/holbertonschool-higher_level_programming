#!/bin/bash
# Bash script that takes in a URL, sends a POST request and displays body
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
