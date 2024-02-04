#!/usr/bin/python3
"""this module prints the first name and last name"""


def say_my_name(first_name, last_name=""):
    """this defines it"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
