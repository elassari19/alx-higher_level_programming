#!/bin/bash
# should takes in a URL and displays all HTTP methods
# should use curl

curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "