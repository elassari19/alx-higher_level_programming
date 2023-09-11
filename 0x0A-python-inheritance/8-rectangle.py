#!/usr/bin/python3
"""defin class
Attributes:
    width: int
    height: int
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        """new instances
        Args:
            width: int
            height: int
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
