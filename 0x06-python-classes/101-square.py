#!/usr/bin/python3
"""square module"""


class Square:
    """function shaping a square object"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        function to get the size attribute
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        function to reset the size attribute
        params:
            value (int): new value to reset
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """
        function to get the position attribute
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        function to reset the position attribute
        params:
            value (int): new value to reset
        """
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value)
                or not all(i >= 0 for i in value)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        finds the area for the square instance
        """
        return self.size ** 2

    def my_print(self):
        """
        function to draw an abstract representation of
        the instance using the pound symbol
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

    def __str__(self):
        """
        function to print the string rep of the square
        """
        return self.my_print()
