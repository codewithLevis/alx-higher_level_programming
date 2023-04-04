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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = self.__width
    
    @property
    def height(self):
      '''Gets the height of the rectangle and returns its integer value'''
        return(self.__height)
    
    @height.setter
    '''sets the height of the rectangle'''
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = self.__height
