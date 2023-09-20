#!/usr/bin/python3
"""defines classe"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square
    Attributes:
        width: int
        height: int
        x: int
        y: int
        id: int
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor
        Args:
            size: int
            x: int
            y: int
            id: int
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size
        Returns:
            int: size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """size
        Args:
            value: int
        """        
        self.width = value
        self.height = value
