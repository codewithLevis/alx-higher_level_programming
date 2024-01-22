#!/usr/bin/python3
"""Module for MyInt subclass"""


def add_attribute(object, attr, value):
    """Adds attribute to an object"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    object.__dict__[attr] = value
