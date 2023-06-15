#!/usr/bin/python3
"""
This module contains a function that indents text
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    Note:
        There should be no space at the beginning or
        at the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    for char in text:
        print(char, end="")
        if char in punctuation_marks:
            print("\n\n", end="")
