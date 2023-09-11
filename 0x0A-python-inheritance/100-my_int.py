#!/usr/bin/python3
"""defin class"""


class MyInt(int):
    """MyInt.
    Args:
        int: int
    """
    def __init__(self, value):
        """new instances
        Args:
            value: int
        """
        self.__value = value

    def __eq__(self, other):
        """equal
        Args:
            other: int
        Returns:
            boolean: true/false.
        """
        return self.__value != other

    def __ne__(self, other):
        """not equal
        Args:
            other: int
        Returns:
            boolean: true/false.
        """
        return self.__value == other
