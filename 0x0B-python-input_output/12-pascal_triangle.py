#!/usr/bin/python3
"""
Module for pascal's triangle function
"""


def pascal_triangle(n):
    """
    function to compute pascal's triangle
    Return: a list of lists of integers
        representing the Pascal's triangle of n
    NOTE: Returns an empty list if n <= 0
        - You can assume n will be always an integer
    """
    triangle = [[1], [1, 1]]
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return triangle

    def new_list(length):
        ref = [0] * length
        ref[0] = 1
        ref[-1] = 1

        return ref

    i = 3

    while i <= n:
        curr_row = new_list(i)
        tmp = 0  # keeps track of previous row
        idx = 1  # keeps track of current row
        prev_row = triangle[i - 2]

        try:
            while tmp < len(prev_row) - 1:
                curr_row[idx] = prev_row[tmp] + prev_row[tmp + 1]

                idx += 1
                tmp += 1
        except IndexError:
            print("error")

        triangle.append(curr_row)
        i += 1

    return triangle
