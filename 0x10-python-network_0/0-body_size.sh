#!/bin/bash
# should displayed the size by bytes

curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
