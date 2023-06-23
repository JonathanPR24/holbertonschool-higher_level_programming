#!/usr/bin/python3

"""
This script adds all command line arguments to a
Python list and saves them to a JSON file.
"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_json_list():
    """
    Add command line arguments to a Python list and save them to a JSON file.
    """
    # Load existing list from file, or create a new empty list
    try:
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_list = []

    # Add command line arguments to the list
    existing_list.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(existing_list, 'add_item.json')

if __name__ == '__main__':
    add_items_to_json_list()
