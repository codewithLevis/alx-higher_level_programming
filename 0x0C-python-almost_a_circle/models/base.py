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
    
    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string 
        representation 'json_string' 
        """
        if json_string is None or json_string == "":
            return []
        else:
            return (json.loads(json_string))
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ +'.json'
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
        except FileNotFoundError:
            return []
        dict_list = cls.from_json_string(json_string)
        instance_list = []
        for dictionary in dict_list:
            instance = cls.create(**dictionary)
            instance_list.append(instance)
        return instance_list