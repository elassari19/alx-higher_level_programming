#!/usr/bin/python3
"""creat class"""


class Rectangle:
    """properties class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init method.
        Args:
            width: int
            height: int
        """
        if (not isinstance(width, int)):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        if (not isinstance(height, int)):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter"""
        if ((self.__width == 0) or (self.__height == 0)):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """str"""
        if (self.__width == 0 or self.__height == 0):
            return ('')
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print(self.print_symbol, end='')
            if (self.__height - 1 != i):
                print('')
        return ("")

    def __repr__(self):
        """repr"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """del"""
        print("{:s}".format("Bye rectangle..."))
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal
        Args:
            rect_1: Rectangle
            rect_2: Rectangle
        Returns:
            Rectangle: Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        return rect_2
