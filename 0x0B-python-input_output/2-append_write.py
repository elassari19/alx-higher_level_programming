#!/usr/bin/python3
"""defin module"""


def append_write(filename="", text=""):
    """append_write
    Args:
        filename: filename
        text: text
    Returns:
        int: int
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """open"""
        return f.write(text)
