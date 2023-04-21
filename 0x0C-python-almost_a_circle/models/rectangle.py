#!/usr/bin/python3
"""
class rectangle inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle constructor function that extends from the Base consructor
    Instance variables that take integer variables
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Gettera and setters functions

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns rectangle's area"""
        return (self.width * self.height)

    def display(self):
        """Desplays the rectangle"""
        for i in range(self.__y):
            print()
        for i in range(0, self.__height):
            print(" " * self.__x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Updates value of the rectangle"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value, in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """string representation of the rectangle"""
        return (f"[Rectangle] ({self.id})\
 {self.x}/{self.y} - {self.width}/{self.height}")

    def to_dictionary(self):
        """
        Returns the dictionary representation of a square instance
        """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
