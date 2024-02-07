#!/usr/bin/python3
"""this module creates the Mylist class and inherits list"""


class MyList(list):
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
