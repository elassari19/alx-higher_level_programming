#!/usr/bin/python3
"""defin module"""


def is_same_class(obj, a_class):
    """is_same_class
    Args:
        obj: object
        a_class: a class

    Returns:
        boolean: true/false.
    """
    return type(obj) == a_class
