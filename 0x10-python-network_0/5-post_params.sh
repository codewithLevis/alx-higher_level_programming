#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL
# displays the body of the response
curl -sL -X POST "$1" -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD"
