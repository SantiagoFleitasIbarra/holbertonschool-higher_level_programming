#!/usr/bin/python3
"""
this module define class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """this defines it"""
    def __init__(self, width, height):
        """initializes the height and width values"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
