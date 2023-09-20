#!/usr/bin/python3
"""defines classe"""
from models.rectangle import Rectangle


from inspect import classify_class_attrs
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
        return ("[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size))

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
        Raises:
            TypeError: is not an integer.
            ValueError: is less than or equal to zero.
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
        """ to_dictionary

        Returns:
            dict: dict
        """
        dict1 = self.__dict__
        dict2 = {}
        dict2['id'] = dict1['id']
        dict2['size'] = dict1['_Rectangle__width']
        dict2['x'] = dict1['_Rectangle__x']
        dict2['y'] = dict1['_Rectangle__y']

        return dict2
