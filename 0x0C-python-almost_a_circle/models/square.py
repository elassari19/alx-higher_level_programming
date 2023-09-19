#!/usr/bin/python3
"""defines classe"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ str """
        return ("[{}] ({}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.size))

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update """
        if args:
            for argmts in range(len(args)):
                if argmts == 0:
                    self.id = args[argmts]
                if argmts == 1:
                    self.size = args[argmts]
                if argmts == 2:
                    self.x = args[argmts]
                if argmts == 3:
                    self.y = args[argmts]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ to_dictionary """
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})