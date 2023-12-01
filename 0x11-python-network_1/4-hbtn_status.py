#!/usr/bin/python3
'''
should sends a request to the URL and displays the value of the variable X-Request-Id
should use the packages requests and sys
'''
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
