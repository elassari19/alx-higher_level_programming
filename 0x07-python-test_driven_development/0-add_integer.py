#!/usr/bin/python3
"""Defines add_integer"""


def add_integer(a, b=98):
    """add_integer
    Args:
        a: int
        b: int
    Raises:
        TypeError: TypeError
    Returns:
        int: int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
