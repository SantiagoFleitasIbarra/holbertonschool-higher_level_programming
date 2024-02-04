#!/usr/bin/python3
"""this module prints a text"""


def text_indentation(text):
    """this defines it"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char_trigger = [":", "?", "."]
    current_line = ''

    for char in text:
        if char in char_trigger:
            print(current_line.strip())
            print()
            current_line = ''
        else:
            current_line += char
    print(current_line.strip(), end='')
