#!/bin/usr/python3

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self._validate_positive_int(width, "width")
        self._validate_positive_int(height, "height")
        self._validate_non_negative_int(x, "x")
        self._validate_non_negative_int(y, "y")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self._validate_positive_int(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_positive_int(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self._validate_non_negative_int(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self._validate_non_negative_int(value, "y")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        if args:
            self._update_attributes(args)
        elif kwargs:
            self._update_attributes(kwargs.values())

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def _validate_positive_int(self, value, attribute):
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute} must be > 0")

    def _validate_non_negative_int(self, value, attribute):
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")

    def _update_attributes(self, values):
        attributes = ["id", "width", "height", "x", "y"]
        for attr, value in zip(attributes, values):
            setattr(self, attr, value if value is not None else getattr(self, attr))
