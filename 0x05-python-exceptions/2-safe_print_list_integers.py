#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    valid_integers = [i for i in my_list[:x] if isinstance(i, int)]
    print("".join(map(str, valid_integers)))
    return len(valid_integers)
