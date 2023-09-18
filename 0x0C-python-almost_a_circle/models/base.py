#!/usr/bin/python3
""" create class """
from os import path
import json


class Base:
    """ base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ __init__ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string """
        new = []
        if list_dictionaries is None:
            return (new)
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file """
        file = "{}.json".format(cls.__name__)
        new = []
        with open(file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            for obj in list_objs:
                new.append(obj.to_dictionary())
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string """
        lst = []
        if json_string is None:
            return (lst)
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            new_c = cls(1, 1)
        if cls.__name__ == "Square":
            new_c = cls(1)
        new_c.update(**dictionary)
        return (new_c)

    @classmethod
    def load_from_file(cls):
        """ load_from_file """
        new_l = []
        rtn_empty = []
        file = "{}.json".format(cls.__name__)
        if path.isfile(file):
            with open(file, 'r') as f:
                new_l = cls.from_json_string(f.read())
            for val in new_l:
                rtn_empty.append(cls.create(**val))
            return (rtn_empty)
