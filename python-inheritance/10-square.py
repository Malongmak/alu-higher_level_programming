#!/usr/bin/python3
"""
Module for Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """
    def __init__(self, size):
        """
        Constructor for the Square class.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
"""
This module implements file checking functionality.
"""

with open("file.txt") as f:
    print("File is present")
