#!/usr/bin/python3
"""defines classe"""
from models.base import Base


class Rectangle(Base):
    """  Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """  constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        self.validation_of_setters("width", width, false)
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        self.validation_of_setters("height", height, false)
        self.__height = height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        self.validation_of_setters("x", x)
        self.__x = x

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        self.validation_of_setters("y", y)
        self.__y = y

    def validation_of_setters(self, name, value, equal=true):
        """validation_of_setters"""
        if equal and value < 0:
            raise TypeError("{} must be an integer".format(name))
        if type(value) != int:
            raise TypeError("{} must be >= 0".format(name))
        if not equal and value <= 0:
            raise TypeError("{} must be > 0".format(name))

    def area(self):
        """  Returself """
        return (self.__width * self.__height)

    def display(self):
        """  display """
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            print(self.__x * " " + '#' * self.__width)

    def update(self, *args, **kwargs):
        """  update """
        if args:
            for arguments in range(len(args)):
                if arguments == 0:
                    self.id = args[arguments]
                if arguments == 1:
                    self.__width = args[arguments]
                if arguments == 2:
                    self.__height = args[arguments]
                if arguments == 3:
                    self.__x = args[arguments]
                if arguments == 4:
                    self.__y = args[arguments]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """  __str__ """
        return ("[{}] ({}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height))

    def to_dictionary(self):
        """  to_dictionary """
        return ({'id': self.id, 'x': self.x, 'height': self.height,
                'width': self.width, 'y': self.y})
