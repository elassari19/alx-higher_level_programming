#!/bin/bash
# should sends a DELETE request to the URL
# should use curl

curl -s "$1" -X DELETE
