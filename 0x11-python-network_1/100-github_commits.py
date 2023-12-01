#!/usr/bin/python3
'''
should takes 2 arguments in order to solve this challenge
should use the packages requests and sys
'''
import sys
import requests


if __name__ == "__main__":
    try:
        repository = sys.argv[1]
        username = sys.argv[2]
        commits = "https://api.github.com/repos/{}/{}/commits" \
            .format(username, repository)
        response = requests.get(commits)
        data = response.json()
        for i, obj in enumerate(data):
            if i == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except ValueError as invalid_json:
        pass
