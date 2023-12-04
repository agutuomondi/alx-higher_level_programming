#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_values = tuple(sum(pair) for pair in zip(tuple_a, tuple_b))
    return sum_values
