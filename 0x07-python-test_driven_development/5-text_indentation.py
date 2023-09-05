#!/usr/bin/python3
"""defines print"""


def text_indentation(text):
    """print
    Args:
        text: str
    Raises:
        TypeError: not str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
