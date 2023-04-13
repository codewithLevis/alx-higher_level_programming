#!/usr/bin/python3
"""Module For is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    '''Returns True if object is an instance of
    a class or subclass else returns False'''
    if isinstance(obj, a_class):
        return (True)

    else:
        for base_class in obj.__class__.__bases__:
            if is_kind_of_class(base_class, a_class):
                return (True)
            return (False)
