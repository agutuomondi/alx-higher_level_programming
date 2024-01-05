#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, heigh=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self._validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_dimension(value, "height")
        self.__height = value

    def _validate_dimension(self, value, dimension):
        """Validate the width and height values."""
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = ["#" * self.__width + "\n" for _ in range(self.__height - 1)]
        rect.append("#" * self.__width)
        return "".join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
