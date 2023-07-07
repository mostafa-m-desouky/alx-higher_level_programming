#!/usr/bin/python3
"""Module for matrix_mul method."""
import numpy as np


def matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    return np.matmul(m_a, m_b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
