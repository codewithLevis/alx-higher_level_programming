#!/usr/bin/python3
"""
base of all classes in the model to manage id attribute
class that inherits from the 'Base' class can use thid 'id'
attribute without a need for creating a separate id management 
system, thus preventing duplication of bugs that might potentially arise
"""

import json

class Base:
    """
    private class attribute that stores the number of 
    instances for each class that inherits from it
    """
    __nb_objects  = 0
            

    """
    Initialize Base instance
    """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
        
    
    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file
        '''
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(dict_list))