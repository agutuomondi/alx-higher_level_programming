#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    def is_valid_matrix(matrix):
        return isinstance(matrix, list) and all(isinstance(row, list) for row in matrix)

    def validate_matrix(matrix, name):
        if not is_valid_matrix(matrix):
            raise TypeError(f"{name} must be a list of lists")
        if not matrix or any(len(row) != len(matrix[0]) for row in matrix):
            raise TypeError(f"Each row of {name} must be of the same size")
        if not all(isinstance(ele, (int, float)) for ele in [num for row in matrix for num in row]):
            raise TypeError(f"{name} should contain only integers or floats")

    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    transposed_b = [list(row) for row in zip(*m_b)]

    new_matrix = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in transposed_b] for row_a in m_a]

    return new_matrix
