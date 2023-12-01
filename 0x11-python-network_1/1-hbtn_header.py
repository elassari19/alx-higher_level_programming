#!/usr/bin/python3
'''
should sends a request to the URL and displays the value of the X-Request-Id
should use the package urllib
'''
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        response = response.info()
        result = response.get('X-Request-Id')
        print(result)
