#!/usr/bin/python3
"""
this module define a function that returns
the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """this defines it"""
    return json.dumps(my_obj)
