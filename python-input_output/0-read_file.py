#!/usr/bin/python3
"""this module define a function that reads a text file"""


def read_file(filename=""):
    """this defines it"""
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
