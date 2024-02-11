#!/usr/bin/python3
"""
this module define a script that adds all arguments to
a Python list, and then save them to a file
"""


import sys
save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file


if __name__ == '__main___':
    filename = 'add_item.json'
    my_list = []

    try:
        my_list.extend(load_json(filename))
    except FileNotFoundError:
        save_json([], filename)

    for element in sys.argv[1:]:
        my_list.append(element)

    save_json(my_list, filename)
    sys.exit(0)
