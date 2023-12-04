#!/usr/bin/python3
def print_matrix_integer(matrix=None):
    if matrix is None:
        matrix = [[]]

    for row in matrix:
        print(' '.join(map('{:d}'.format, row)))
