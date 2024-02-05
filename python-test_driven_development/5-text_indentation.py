#!/usr/bin/python3
"""this module prints a text"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each '.', '?', and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_paragraph = True
    for char in text:
        if new_paragraph and char.isspace():
            continue

        print(char, end='')

        if char in ['.', '?', ':']:
            print('\n')
            new_paragraph = True
        else:
            new_paragraph = False
