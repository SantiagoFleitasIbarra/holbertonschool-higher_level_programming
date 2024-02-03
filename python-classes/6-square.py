#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("Position must be a tuple of 2 positive integers")

        self._position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
