#!/bin/bash
# should sends a request, and displays only the status code of the response
# not allowed to use any pipe, redirection, etc
# not allowed to use ; and &&
# should use curl

curl -sLw "%{http_code}" -o /dev/null "$1"
