#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    if my_list is None:
        my_list = []
    result = ""
    ret = 0
    for i in range(x):
        try:
            result += "{:d}".format(my_list[i])
            ret += 1
        except (ValueError, TypeError):
            continue
    print(result)
    return ret
