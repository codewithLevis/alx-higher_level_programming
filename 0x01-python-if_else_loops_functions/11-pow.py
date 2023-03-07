#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    for i in range(b):
        result *= a
    return result
