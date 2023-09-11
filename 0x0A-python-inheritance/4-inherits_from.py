#!/usr/bin/python3
"""defin module"""


def inherits_from(obj, a_class):
    """inherits_from
    Args:
        obj: object
        a_class: a class

    Returns:
        boolean: true/false.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
