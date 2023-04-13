#!/usr/bin/python3
"""Module For is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    '''Returns True if object is an instance of
    a class or subclass else returns False'''
    if isinstance(obj, a_class):
        return (True)

    else:
        return (False)
