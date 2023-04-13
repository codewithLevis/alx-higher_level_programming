#!/usr/bin/python3
"""Module For is_kind_of_class"""


def inherits_from(obj, a_class):
    '''Returns True if the object is an 
    instance of a class, else returns false'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)