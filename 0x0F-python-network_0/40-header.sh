#!/bin/bash
# Bash script that sends a GET request to the URL, and displays the body
curl -sL "GET" -H "X-HolbertonSchool-User-Id: 98" "$1"
