#!/usr/bin/python3
"""
this module returns True if the object
is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """this defines it"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
