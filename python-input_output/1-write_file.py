#!/usr/bin/python3
"""this module define a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """this defines it"""
    with open(filename, mode='w', encoding='utf-8') as file:
        num_chr = file.write(text)
        return num_chr
