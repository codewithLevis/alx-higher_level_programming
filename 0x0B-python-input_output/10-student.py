#!/usr/bin/python3

class Student:
  """Initialize student attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
      """the method retrieves all attributes if none is provides. 
         Else it filters the list of attributes to include only those that are specified in the attrs list.
      """
        json_dict = {}
        if attrs is None:
            attrs = [attr_name for attr_name in dir(self) if not callable(getattr(self, attr_name))]
        """iterates over the filtered list of attributes and adds 
           any serializable attributes (strings and integers) to the json_dict dictionary.
        """
        for attr_name in attrs:
            if hasattr(self, attr_name):
                attr_value = getattr(self, attr_name)
                if isinstance(attr_value, (str, int)):
                    json_dict[attr_name] = attr_value
        return (json_dict)
