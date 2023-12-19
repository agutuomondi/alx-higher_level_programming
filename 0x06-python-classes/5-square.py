#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self._size = None  # Use a single underscore for protected attribute
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self._validate_size(value)
        self._size = value

    def area(self):
        """Return the current area of the square."""
        return self._size * self._size

    def my_print(self):
        """Print the square with the # character."""
        for _ in range(self._size):
            print("#" * self._size)
        if self._size == 0:
            print("")

    def _validate_size(self, value):
        """Validate the size argument."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
