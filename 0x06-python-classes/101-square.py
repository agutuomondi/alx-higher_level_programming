#!/usr/bin/python3

class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        self._validate_size(value)
        self._size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        self._validate_position(value)
        self._position = value

    def _validate_size(self, value):
        """Validate the size.

        Args:
            value (int): The size value to validate.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def _validate_position(self, value):
        """Validate the position.

        Args:
            value (tuple): The position value to validate.

        Raises:
            TypeError: If the position is not a tuple of 2 integers.
            ValueError: If any element in the tuple is less than 0.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the current area of the square."""
        return self._size * self._size

    def my_print(self):
        """Print the square with the # character."""
        if self._size == 0:
            print("")
            return

        for _ in range(self._position[1]):
            print("")

        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)

    def __str__(self):
        """Define the print() representation of a Square."""
        representation = ""
        if self._size != 0:
            representation += "\n" * self._position[1]

        for _ in range(self._size):
            representation += " " * self._position[0] + "#" * self._size + "\n"

        return representation
