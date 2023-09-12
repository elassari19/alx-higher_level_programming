#!/usr/bin/python3
"""defin module"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file
    Args:
        my_obj: my_obj
        filename: filename
    Returns:
        type: type
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """open"""
        json_object = json.dumps(my_obj)
        f.write(json_object)
        f.close()
