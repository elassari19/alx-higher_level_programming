#!/usr/bin/python3
'''
should takes your GitHub credentials (username and password)
should use Basic Authentication with a personal access token as password
'''
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    data = response.json()
    print(data.get("id"))
