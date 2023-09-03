#!/usr/bin/python3
"""
Module for a function that finds
a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    '''
    description:  function that finds
        a peak in a list of unsorted integers.
    params:
        list_of_integers: list object only ofr intergers
    '''
    leng = list_of_integers.__len__()
    if leng == 0:
        return None
    low = 0
    high = leng - 1

    while low <= high:
        mid = (low + high) // 2
        digit = list_of_integers[mid]

        if (mid == 0 or digit >= list_of_integers[mid - 1]) \
                and (mid == leng - 1 or digit >= list_of_integers[mid + 1]):
            return digit
        elif mid < leng - 1\
                and list_of_integers[mid + 1] > digit:
            low = mid + 1
        else:
            high = mid - 1

    return None
