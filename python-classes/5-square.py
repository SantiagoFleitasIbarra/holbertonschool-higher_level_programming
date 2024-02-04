#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
    pass
