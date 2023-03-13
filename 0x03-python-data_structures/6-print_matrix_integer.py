#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for column in range(len(raw)):
            if column < len(raw) - 1:
                print('{}'.format(raw[column]), end=' ')
            else:
                print('{}'.format(raw[column]), end='')
        print()
