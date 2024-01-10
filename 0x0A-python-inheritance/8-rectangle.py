#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
from typing import Union


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width: int, height: int):

        super().__init__()
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """Set the width of the Rectangle."""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self) -> int:
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """Set the height of the Rectangle."""
        self.integer_validator("height", value)
        self.__height = value

    def area(self) -> int:
        """Calculate the area of the Rectangle."""
        return self.__width * self.__height
