#!/bin/bash
# should sends a request, and displays only the status code of the response
curl -sLw "%{http_code}" -o /dev/null "$1"
