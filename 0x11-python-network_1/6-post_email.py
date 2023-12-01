#!/usr/bin/python3
'''
should takes in a URL, sends a request to the URL and displays the body of the response
should use the packages requests and sys
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    params = {
        "email": email
    }
    response = requests.post(url, data=params)
    print(response.text)
