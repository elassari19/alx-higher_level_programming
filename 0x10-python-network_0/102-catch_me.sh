#!/bin/bash
# should request to 0.0.0.0:5000/catch_me that causes the server to respond
# should use curl
# not allow to use echo, cat

curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -d "user_id=98" -H "Origin:School"
