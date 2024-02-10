#!/usr/bin/python3
"""this module returns True or False"""


def inherits_from(obj, a_class):
    """this defines it"""
    return issubclass(type(obj), a_class) and type(obj) != a_class