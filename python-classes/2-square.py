#!/usr/bin/python3
class Square:
    """
    A class representing a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size
