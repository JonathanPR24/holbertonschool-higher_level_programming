#!/usr/bin/python3

"""
This module contains a function for reading a text
file and printing its content to stdout.
"""


def read_file(filename=""):
    """
    Read a text file and print its content to stdout.

    Args:
        filename (str): The name of the file to be read. (default "")
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
