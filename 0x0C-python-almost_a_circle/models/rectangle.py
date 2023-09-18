#!/usr/bin/python3
"""defines classe"""


from models.base import Base


class Rectangle(Base):
    """Rectangle
     Attributes:
        width: int
        height: int
        x: int
        y: int
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__
        Args:
            width: int
            height: int
            x: int
            y: int
            id: int
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """__str__"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        """width
        Returns:
            int: int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width

        Args:
            value: int

        Raises:
            TypeError: is not integer
            ValueError: is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height
        Returns:
            int: int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height
        Args:
            value: int
        Raises:
            TypeError: is not an integer
            ValueError: is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x
        Returns:
            int: int
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set x

        Args:
            value: int

        Raises:
            TypeError: is not an integer
            ValueError: is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y
        Returns:
            int: int
        """
        return self.__y

    @y.setter
    def y(self, value):
        """set y
        Args:
            value: int
        Raises:
            TypeError: is not an integer
            ValueError: is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area
        Returns:
            int: int
        """
        return self.__width * self.__height

    def display(self):
        """display"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update

        Args:
            *args: arguments
            **kwargs: kwargs
        """
        if args is not None and len(args) is not 0:
            list_atrr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atrr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary
        Returns:
            dict: dict
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
