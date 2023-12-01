#!/usr/bin/python3
'''
should takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
should sent in the variable q
'''
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    query = {"q": q}
    response = requests.post(url, data=query)
    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            data_id = data.get("id")
            data_name = data.get("name")
            print("[{}] {}".format(data_id, data_name))
    except ValueError as invalid_json:
        print("Not a valid JSON")
