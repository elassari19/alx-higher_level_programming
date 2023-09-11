#!/usr/bin/python3
"""defin class

Attributes:
    width: int
    height: int
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square.

    Args:
        Rectangle: rectangle
    """

    def __init__(self, size):
        """new instances
        Args:
            size: size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """string
        Returns:
            str: string
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """area
        Returns:
            int: int
        """
        return self.__size ** 2
