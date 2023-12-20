#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = self.validate_radius(radius)

    @property
    def radius(self):
        """Get the radius of the MagicClass."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the MagicClass.

        Args:
            value (float or int): The new radius value.
        """
        self.__radius = self.validate_radius(value)

    def validate_radius(self, value):
        """Validate and set the radius.

        Args:
            value (float or int): The radius value to validate.

        Returns:
            float: The validated radius value.

        Raises:
            TypeError: If the radius is not a number.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        return float(value)

    def area(self):
        """Return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius


# Example usage:
if __name__ == "__main__":
    magic_circle = MagicClass(radius=5)
    print(f"Area: {magic_circle.area()}")
    print(f"Circumference: {magic_circle.circumference()}")



































































