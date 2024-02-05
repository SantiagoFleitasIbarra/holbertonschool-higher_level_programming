#!/usr/bin/python3
"""this module defines a rectangle class"""


class Rectangle:
    """this defines the class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
            return perimeter
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height != 0 and self.__width != 0:
            symbol = "#"
            return "\n".join([self.__width * symbol] * self.__height)
        else:
            return ""

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
