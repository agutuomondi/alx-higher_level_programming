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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, side_length):
        """Create a square Rectangle.

        Args:
            side_length (int): The side length of the square.
        """
        return cls(side_length, side_length)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = [str(self.print_symbol) * self.__width + "\n" for _ in range(self.__height - 1)]
        rect.append(str(self.print_symbol) * self.__width)
        return "".join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

# Example usage
rectangle1 = Rectangle(3, 4)
square1 = Rectangle.square(5)
print(rectangle1)
print(square1)
print(f"Number of instances: {Rectangle.number_of_instances}")  # Output: 2
del rectangle1
print(f"Number of instances: {Rectangle.number_of_instances}")  # Output: 1
del square1
print(f"Number of instances: {Rectangle.number_of_instances}")  # Output: 0
