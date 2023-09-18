#!/usr/bin/python3
"""defines classe"""


from models.rectangle import Rectangle
from inspect import classify_class_attrs


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
        """__init__
        Args:
            size: int
            x: int
            y: int
            id: int
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """size
        Returns:
            int: int
        """
        return self.width

    @size.setter
    def size(self, value):
        """set size
        Args:
            value: int
        Raises:
            TypeError: is not an integer
            ValueError: is less than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update
        Args:
            *args: arguments
            **kwargs: dictionary
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary
        Returns:
            dict: dict
        """
        a_dict = {"id": 0, "size": 0, "x": 0, "y": 0}
        for key in a_dict:
            if key == "id":
                a_dict[key] = self.id
            elif key == "size":
                a_dict[key] = self.width
                a_dict[key] = self.height
            elif key == "x":
                a_dict[key] = self.x
            elif key == "y":
                a_dict[key] = self.y

        return a_dict
