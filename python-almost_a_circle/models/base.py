#!/usr/bin/python3
"""this module define a class Base"""


import json


class Base:
    """this define a class constructor"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
