#!/bin/bash
# should sends a JSON POST request to a URL
# should send a POST request with the contents of a file
# should use curl

curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
