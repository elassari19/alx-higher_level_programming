#!/usr/bin/python3
"""defin module"""


def write_file(filename="", text=""):
    """write_file
    Args:
        filename: filename
        text: text
    Returns:
        int: int
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """open"""
        return f.write(text)
