#!/usr/bin/python3
"""this module define a class Base"""


class Base:
    """this define a class constructor"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
