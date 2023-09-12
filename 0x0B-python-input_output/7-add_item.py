#!/usr/bin/python3
"""defin module"""
from sys import argv


load_json_file = __import__('6-load_from_json_file').load_from_json_file
save_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    _list = load_json_file('add_item.json')
except (ValueError, FileNotFoundError):
    _list = []

for i in argv[1:]:
    _list.append(i)

save_json_file(_list, 'add_item.json')
