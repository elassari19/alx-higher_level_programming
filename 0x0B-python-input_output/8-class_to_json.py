#!/usr/bin/python3
"""defin module"""


def class_to_json(obj):
    """class_to_json
    Args:
        obj: obj
    Returns:
        dict: dict
    """
    return obj.__dict__
