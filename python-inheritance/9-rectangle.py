#!/usr/bin/python3
"""
this module define class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """this defines it"""
    def __init__(self, width, height):
        """initializes the height and width values"""
        self.__width = 0
        self.__height = 0
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__height * self.__width
