#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
from typing import Union


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width: int, height: int):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
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

    def __str__(self) -> str:
        """Return the string representation of a Rectangle."""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
