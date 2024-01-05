#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self._set_dimensions(width, height)

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

    def _set_dimensions(self, width, height):
        """Set width and height."""
        self.width = width
        self.height = height

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
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not all(isinstance(rect, Rectangle) for rect in (rect_1, rect_2)):
            raise TypeError("Both rect_1 and rect_2 must be instances of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return cls(size, size)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        return "\n".join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
