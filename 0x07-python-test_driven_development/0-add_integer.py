#!/usr/bin/python3
def add_integer(a, b=98):
    for num in (a, b):
        if not isinstance(num, (int, float)):
            raise TypeError(f"{num} must be an integer or float")
    return int(a) + int(b)
