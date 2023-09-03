#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response
status_code=$(curl -s -o /dev/null -w "%{http_code}" -L "$1")

if [ "$status_code" == 200 ]; then
	response=$(curl -s -L "$1")
	echo "$response"
fi
