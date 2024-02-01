#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_sort = sorted(a_dictionary.keys())
    for key in key_sort:
        value = a_dictionary[key]
        print(f"{key}: {value}")
