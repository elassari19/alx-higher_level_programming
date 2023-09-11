#!/usr/bin/python3
"""defin class"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """area
        Raises:
            Exception: Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator
        Args:
            name: string
            value: int

        Raises:
            TypeError: TypeError
            ValueError: ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
