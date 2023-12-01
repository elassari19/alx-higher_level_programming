#!/usr/bin/python3
'''
should sends a request to the URL and displays the body of the response
should manage urllib.error.HTTPError exceptions and print: Error code:
should use the packages urllib and sys
'''
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response = response.read().decode("utf-8")
            print(response)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
