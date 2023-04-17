#!/usr/bin/python3

"""
module for the square class that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    class that defines a square as a special rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instialize a Square instance with size, x, y and id
        """
        super().__init__(size, size, x, y, id)

    
    def __str__(self):
        """
        Returns a string representation of the Square instance
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, 
        self.y, self.width))
    
    @property
    def size(self):
        """
        Getter method for the size attribute
        """
        return self.width
    
    @size.Getter
    def size(self, value):
        """sets the size attribute"""
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute of the Square instance
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, args in enumerate(args):
                setattr(self, attributes[i], arg)
        
        else:
            for key, value, in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """
        Returns the dictionary representation of a square instance
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}