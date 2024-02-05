#!/usr/bin/python3
"""this module defines the sum of a and b"""


def add_integer(a, b=98):
    """this define a sum of a and b"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
