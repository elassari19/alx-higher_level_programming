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
        new_list = []
        if list_dictionaries is None:
            return (new_list)
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file """
        file = "{}.json".format(cls.__name__)
        new_list = []
        with open(file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string """
        new_list = []
        if json_string is None:
            return (new_list)
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            new_class = cls(1, 1)
        if cls.__name__ == "Square":
            new_class = cls(1)
        new_class.update(**dictionary)
        return (new_class)

    @classmethod
    def load_from_file(cls):
        """ load_from_file """
        new_list = []
        rtn_empty = []
        file = "{}.json".format(cls.__name__)
        if path.isfile(file):
            with open(file, 'r') as f:
                new_list = cls.from_json_string(f.read())
            for val in new_list:
                rtn_empty.append(cls.create(**val))
            return (rtn_empty)
