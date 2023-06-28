#!usr/bin/python3
"""
This module contains the Base class.
"""


from models.base import Base

class Rectangle(Base):
    """
    Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): id to assign to the instance. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getter and setter for width
    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        self.__height = value

    # Getter and setter for x-coordinate
    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position"""
        self.__x = value

    # Getter and setter for y-coordinate
    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position"""
        self.__y = value
