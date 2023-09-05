#!/usr/bin/python3
"""defines multiplie using NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul
    Args:
        m_a: matrix
        m_b: matrix
    Returns:
        matrix: matrix
    """
    return np.matmul(m_a, m_b)
