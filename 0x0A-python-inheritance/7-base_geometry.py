#!/usr/bin/python3
"""Module For BaseGeometry"""


class BaseGeometry:
    """Geometry Class"""
    def area(self):
        '''Raise exception'''
        raise Exception("area() is not implimented")

    def integer_validator(self, name, value):
        '''Raise TypeError if value is not an integer'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            '''Raise valueError if value is negative or zero'''
            raise ValueError(f"{name} must be greater than 0")