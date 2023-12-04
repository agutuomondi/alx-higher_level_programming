#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        return my_list[:idx] + [element] + my_list[idx + 1:]
    else:
        return my_list
