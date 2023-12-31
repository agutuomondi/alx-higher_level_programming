#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = sum(tup[0] * tup[1] for tup in my_list)
    den = sum(tup[1] for tup in my_list)

    return num / den
