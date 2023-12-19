#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self._size = None  # Use a single underscore for protected attribute
        self._position = None  # Use a single underscore for protected attribute
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self._validate_size(value)
        self._size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        self._validate_position(value)
        self._position = value

    def area(self):
        """Return the current area of the square."""
        return self._size * self._size

    def my_print(self):
        """Print the square with the # character."""
        if self._size == 0:
            print("")
            return

        for _ in range(self._position[1]):
            print()

        for _ in range(self._size):
            print(" " * self._position[0], end="")
            print("#" * self._size)

    def _validate_size(self, value):
        """Validate the size argument."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def _validate_position(self, value):
        """Validate the position argument."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
