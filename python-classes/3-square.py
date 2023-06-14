#!/usr/bin/python3
"""A class that defines a square is included in this module. """


class Square:
    """square attribute definition"""

    def __init__(self, size=0):
        """Initialize"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Square area to which you came"""
        return self.__size ** 2
