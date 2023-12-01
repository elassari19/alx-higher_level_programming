#!/usr/bin/python3
'''
should takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
should sent in the variable q
'''
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    result = response.text
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(result)
