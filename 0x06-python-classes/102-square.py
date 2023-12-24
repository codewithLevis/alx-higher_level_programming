#!/usr/bin/python3

"""square module"""


class Square:
    """function shaping a square object"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        returns the size of the squre object
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        resets the size attribute
        Param:
            value (int): new value
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        finds the area of the square instance
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        function to check for equality of square instances
        Param:
            other (Square): value to compare
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        function to check for equality of square instances
        Param:
            other (Square): value to compare
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        function to check for less than of square instances
        Param:
            other (Square): value to compare
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        function to check for less thatn or
            equality of square instances
        Param:
            other (Square): value to compare
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        function to check for greater than of square instances
        Param:
            other (Square): value to compare
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        function to check for greater than or
            equality of square instances
        Param:
            other (Square): value to compare
        """
        if isinstance(other, Square):
            return(self.area() >= other.area())
        return NotImplemented
