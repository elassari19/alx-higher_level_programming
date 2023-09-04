#!/usr/bin/python3
"""creat class"""


class Rectangle:
    """
    properties class
    Attributes:
        width: int
        height: int
    """
    def __init__(self, width=0, height=0):
        """init method.
        Args:
            width: int
            height: int
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width
        Returns:
            int: int
        """
        return self.__width

    @property
    def height(self):
        """Height
        Returns:
            int: int
        """
        return self.__height

    @width.setter
    def width(self, value):
        """set width
        Args:
            value: number
        Raises:
            TypeError: TypeError
            ValueError: ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """set height
        Args:
            value: int
        Raises:
            TypeError: TypeError
            ValueError: ValueError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
