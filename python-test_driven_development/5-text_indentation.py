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
        This function indents the text by adding two new lines after each occurrence of the characters ".", "?", and ":".
        Leading and trailing spaces are stripped from each character before printing.

    Example:
        >>> text_indentation("Hello! How are you? I am fine.")
        Hello!
        How are you?
        I am fine.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    for i, char in enumerate(text):
        char = char.strip()
        print(char, end="")
        if char in punctuation_marks and i < len(text) - 1:
            next_char = text[i + 1]
            if not next_char.isspace():
                print("\n\n", end="")
