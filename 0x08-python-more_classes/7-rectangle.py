#!/usr/bin/python3
class Rectangle:
    '''initialize the class attribute'''
    number_of_instances = 0
    '''initialize the instance attributes of the Rectangle'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        '''increment instance count'''
        type(self).number_of_instances += 1
        
    '''delete an instance'''
    def __del__(self):
        print("Bye rectangle...")
        '''decrement instance count'''
        type(self).number_of_instances -= 1
        
    '''Set Rectangle attributes as private'''
    @property
    def width(self):
        return(self.__width)
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        '''Gets the height of the rectangle and returns its integer value'''
        return(self.__height)
    
    @height.setter
    
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        
        return(2 * (self.__width + self.__height))
   
    def area(self):
        return(self.__width * self.__height)
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return("")
        rectangle = '#'
        for i in range(self.__width):
            rectangle = rectangle * self.__height
        
            if i != (self.__width - 1):
                print("")
        return(rectangle)
    
    def __repr__(self):
        return(f"Rectangle({self.width}, {self.height})")
