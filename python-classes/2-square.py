#!/usr/bin/python3
"""Class representing a square"""
class Square:
    def __init__(self, size=0):
        """Initializes a new square"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size
