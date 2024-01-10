#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
from typing import Union


class BaseGeometry:
    """Represent base geometry."""

    @classmethod
    def integer_validator(cls, name: str, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Square(BaseGeometry):
    """Represent a square."""

    def __init__(self, size: int):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self) -> int:
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """Set the size of the square."""
        self.integer_validator("size", value)
        self.__size = value

    def area(self) -> int:
        """Calculate the area of the square."""
        return self.__size ** 2
