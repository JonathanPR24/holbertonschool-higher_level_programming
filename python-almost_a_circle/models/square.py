#!/usr/bin/python3
"""
This module contains the Base class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the square's position. Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of the Square.

        Returns:
            str: The string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
     @property
    def size(self):
        """
        Getter for size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size.

        Args:
            value (int): The value to set as the size of the square.
        """
        self.width = value
        self.height = value
