#!/bin/bash
# should takes in a URL as an argument, sends a GET request to the URL
# header variable X-School-User-Id must be sent with the value 98
# should use curl

curl -s "$1" -H "X-School-User-Id: 98"
