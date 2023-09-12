#!/usr/bin/python3
"""defin module"""


def read_file(filename=""):
    """read_file
    Args:
        filename: filename
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
