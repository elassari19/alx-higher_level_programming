#!/bin/bash
# should displayed the size by bytes
# should use curl

curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
