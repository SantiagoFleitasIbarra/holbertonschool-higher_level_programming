#!/usr/bin/python3
"""
this module define a function that returns
an object (Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """this defines it"""
    return json.loads(my_str)
