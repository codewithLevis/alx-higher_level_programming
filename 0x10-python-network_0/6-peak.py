#!/usr/bin/python3
"""
Module for a function that finds
a peak in a list of unsorted integers.
"""
def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    low = 0
    high = list_of_integers.__len__() - 1

    while low <= high:
        mid = (low + high) // 2
        digit = list_of_integers[mid]

        if digit >= list_of_integers[mid - 1] and digit >= list_of_integers[mid + 1]:
            return digit
        elif list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1


