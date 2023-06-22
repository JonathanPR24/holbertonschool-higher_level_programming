#!/usr/bin/python3

"""
This module contains a function for appending a string to the
end of a text file and returning the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file and return
    the number of characters added.

    Args:
        filename (str): The name of the file to append to. (default "")
        text (str): The string to append to the file. (default "")

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
