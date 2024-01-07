#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    for name in (first_name, last_name):
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")
    print(f"My name is {first_name} {last_name}")
