#!/usr/bin/python3
class Square:
    """
    Class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size
