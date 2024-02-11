#!/usr/bin/python3
"""
this module define a function that returns the dictionary description
with simple data structure for JSON serialization of an objec
"""


import json


def class_to_json(obj):
    """this defines it"""
    return obj.__dict__
