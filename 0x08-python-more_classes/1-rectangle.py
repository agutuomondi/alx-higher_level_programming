#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width: int = 0, height: int = 0):

        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Get/set the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self) -> int:
        """Get/set the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
