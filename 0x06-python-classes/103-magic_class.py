#!/usr/bin/python3
"""define class"""
import math


class MagicClass:
    """properties
    Attributes:
        radius: radius
    """
    def __init__(self, radius=0):
        """instances

        Args:
            radius: radius

        Raises:
            TypeError: number
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
