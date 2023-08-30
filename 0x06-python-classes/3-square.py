#!/usr/bin/python3
"""defines class"""


class Square:
    """
    properties

    Attributes:
        size: size
    """
    def __init__(self, size=0):
        """instances

        Args:
            size: size
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """square size

        Returns: area size
        """
        return self.__size ** 2
