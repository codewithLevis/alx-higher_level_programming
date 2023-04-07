#!/usr/bin/python3
"""Module for Matrix Multiplication"""


def is_empty(li):
    """Checking for empty matrix or empty list in it"""
    if len(li) == 0:
        return False
    for i in li:
        if len(i) == 0:
            return False
    return True


def matrix_mul(m_a, m_b):
    """ a function that multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if not is_empty(m_a):
        raise ValueError('m_a can\'t be empty')
    if not is_empty(m_b):
        raise ValueError('m_b can\'t be empty')

    if not all(isinstance(val, (int, float)) for row in m_a for val in row):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(val, (int, float)) for row in m_b for val in row):
        raise TypeError('m_b should contain only integers or floats')

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    # check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    new = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new[i][j] += m_a[i][k] * m_b[k][j]

    return new
