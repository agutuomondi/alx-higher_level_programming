#!/usr/bin/python3
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    a_np = np.array(m_a)
    b_np = np.array(m_b)
    result_np = np.matmul(a_np, b_np)
    result_list = result_np.tolist()
    return result_list
