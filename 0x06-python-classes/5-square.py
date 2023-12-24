#!/usr/bin/python3

"""square module"""


class Square:
    """function shaping a square object"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        returns size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        resets the value of the instance
        param:
            value (int): new value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        finds the area of the instance
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints abstract representation of the
        function using the pound symbol
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
