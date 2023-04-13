#!/usr/bin/python3
"""Module for Square subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class square(Rectangle):
    """Class square that inherits from Rectangle"""
    def __init__(self, size):
        self.__size = 0
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return(f"[Square] {self.__size}/{self.__size}")
