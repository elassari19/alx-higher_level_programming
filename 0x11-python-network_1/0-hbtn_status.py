#!/usr/bin/python3
'''
should fetche data from https://alx-intranet.hbtn.io/status
should use the package urllib
'''
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        response = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(response)))
        print('\t- content: {}'.format(response))
        print('\t- utf8 content: {}'.format(response.decode("utf-8")))
