#!/usr/bin/python3
def add_attribute(obj, att, value):
    try:
        obj.__dict__[att] = value
    except AttributeError:
        raise TypeError("can't add new attribute")
