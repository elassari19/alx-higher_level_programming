#!/usr/bin/python3
'''
should email, sends a POST request to the passed URL
should sent in the email variable
should use the packages urllib and sys
'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {
        "email": email
    }
    query_string = urllib.parse.urlencode(params)
    data = query_string.encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        # If you do not pass the data argument, urllib uses a GET request.
        # One way in which GET and POST requests differ is that POST requests
        # often have "side-effects".
        response = response.read().decode("utf-8")
        print(response)
