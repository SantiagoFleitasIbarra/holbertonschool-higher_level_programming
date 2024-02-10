#!/usr/bin/python3
"""
this module define a class
Square that inherits from Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """this defines it"""
    def __init__(self, size):
        """initializes the size value"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
