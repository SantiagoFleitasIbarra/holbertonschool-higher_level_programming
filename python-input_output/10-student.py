#!/usr/bin/python3
"""this module define a class Student that defines a student"""


class Student:
    """this defines the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            select_attrs = {}
            for attr in attrs:
                if hasattr(self, attr):
                    select_attrs[attr] = getattr(self, attr)
            return select_attrs
