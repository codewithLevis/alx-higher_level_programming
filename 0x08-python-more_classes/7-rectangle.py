#!/usr/bin/python3
"""Elevating my rectangle's functionality"""


class Rectangle:
    '''initialize the class attribute'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return self._width * self._height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self._width == 0 or self._height == 0:
            return 0
        else:
            return 2 * (self._width + self._height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return("")
        rectangle = ""
        for i in range(self.height):
            rectangle += str(self.print_symbol) * self.width
            if i != self.height - 1:
                rectangle += '\n'
        return(rectangle)

    def __repr__(self):
        """Returns a string representation of
        the rectangle that can be used to recreate a new instance"""

        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        """Deletes an instance of a rectangle"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
