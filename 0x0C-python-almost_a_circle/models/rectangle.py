#!/usr/bin/python3
from models.base import Base
"""
class rectangle inherits from Base
"""


class Rectangle(Base):
    """
    Rectangle constructor function that extends from the Base consructor
    Instance variables that take integer variables
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = 0
        self.__y = 0
    
    #Gettera and setters functions

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

    """
    Retuns:
        int: area of the rectangle
    """
    def area(self):
        return (self.width * self.height)
    
    """
    print the string representation of the rectangle insyance
    using the # character
    """

    def display(self):
        for i in range(self.__y):
            print()
        for i in range(0, self.__height):
            print(" " * self.__x + "#" * self.width)

    
    """
    Assigns an argument to each attribute using the 
    non-key word argument syntax *args and keyword **kwargs
    """
    def update(self, *args,):
        """
        Interate over the arguments to assign each argument 
        to the appropriate attribute, i.e. arguments are passed 
        in the correct order ('id', 'width', 'height', 'x', 'y')
        """
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
    
    """
    def update(self, *args, **kwargs):
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        
        else:
            for key, value, in kwargs.items():
                setattr(self, key, value)
    """

    """
    Overides the __str__ method
    Returns:
        str: string representation of the rectangle
    """

    def __str__(self):
        return (f"[Rectangle] {(self.id)} 
        {self.x}/{self.y} - {self.width}/{self.height}")
    

    def to_dictionary(self):
        """
        Returns the dictionary representation of a square instance
        """
        return {"id": self.id, "width": self.width, 
        "height": self.height, "x": self.x, "y": self.y}