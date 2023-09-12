#!/usr/bin/python3
"""defin module"""
import json


def load_from_json_file(filename):
    """load_from_json_file
    Args:
        filename: filename
    Returns:
        object: object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
