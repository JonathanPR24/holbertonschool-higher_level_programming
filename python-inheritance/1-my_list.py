#!/usr/bin/python3
"""Module to define MyList class"""


class MyList(list):
    """
    Custom list class that inherits from the built-in list class.

    Public Methods:
        print_sorted(): Prints the list in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
