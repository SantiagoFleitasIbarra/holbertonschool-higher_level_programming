#!/usr/bin/python3
"""
this module define a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """this defines it"""
    with open(filename, mode='a', encoding='utf-8') as file:
        new_chr = file.write(text)
        return new_chr
