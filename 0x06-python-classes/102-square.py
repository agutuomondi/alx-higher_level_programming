#!/usr/bin/python3

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self._size = self._validate_size(size)

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        self._size = self._validate_size(value)

    def _validate_size(self, value):
        """Validate and set the size.

        Args:
            value (int): The size value to validate.

        Returns:
            int: The validated size value.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        return value

    def area(self):
        """Return the current area of the square."""
        return self._size * self._size

    def __eq__(self, other):
        """Define the == comparison to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a Square."""
        return self.area() >= other.area()
