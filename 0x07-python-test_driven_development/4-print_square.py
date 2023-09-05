#!/usr/bin/python3
"""defines square"""


def print_square(size):
    """print
    Args:
        size: int
    Raises:
        TypeError: not integer
        ValueError: < 0
    """
    message = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError(message)

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError(message)

    for i in range(size):
        print("#" * size)
