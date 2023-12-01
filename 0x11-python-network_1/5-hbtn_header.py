#!/usr/bin/python3
'''
should takes in a URL and an email address, sends a POST request
should sent in the variable email
should use the packages requests and sys
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    result = response.headers.get("X-Request-Id")
    print(result)
