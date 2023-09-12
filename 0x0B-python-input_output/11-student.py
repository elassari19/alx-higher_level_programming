#!/usr/bin/python3
"""defin class"""


class Student:
    """Student
    Attributes:
        first_name: first_name
        last_name: last_name
        age: age
    """
    def __init__(self, first_name, last_name, age):
        """__init__
        Args:
            first_name: first_name
            last_name: last_name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json
        Returns:
            dict: dict
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """reload_from_json
        Args:
            json: json
        """
        self.__dict__.update(json)
