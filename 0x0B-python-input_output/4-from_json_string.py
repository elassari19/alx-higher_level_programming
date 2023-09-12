#!/usr/bin/python3
"""defin module"""
import json


def from_json_string(my_str):
    """from_json_string
    Args:
        my_str: my_str
    Returns:
        type: type
    """
    return json.loads(my_str)
