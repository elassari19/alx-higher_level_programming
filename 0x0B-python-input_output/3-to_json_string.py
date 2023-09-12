#!/usr/bin/python3
"""defin module"""
import json


def to_json_string(my_obj):
    """to_json_string
    Args:
        my_obj: my_obj
    Returns:
        str: string
    """
    return json.dumps(my_obj)
