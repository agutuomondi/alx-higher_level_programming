#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self._validate_size(size)
        self._size = size

    @property
    def size(self):
        """Getter for size."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for size."""
        self._validate_size(value)
        self._size = value

    def area(self):
        """Return the current area of the square."""
        return self._size * self._size

    def _validate_size(self, size):
        """Validate the size argument."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
