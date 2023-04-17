#!/usr/bin/python3

"""Class student"""
class Student:
    """
    Defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the given first name, last name, and age.
        
        :param first_name: The student's first name.
        :param last_name: The student's last name.
        :param age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of this Student instance.
        
        If attrs is not None and is a list of strings, only the attributes with names contained in the list
        will be retrieved. Otherwise, all attributes will be retrieved.
        
        :param attrs: An optional list of attribute names to retrieve.
        :return: A dictionary containing the serialized attributes of this Student instance.
        """
        json_dict = {}
        if attrs is None:
            attrs = [attr_name for attr_name in dir(self) if not callable(getattr(self, attr_name))]
        for attr_name in attrs:
            if hasattr(self, attr_name):
                attr_value = getattr(self, attr_name)
                if isinstance(attr_value, (str, int)):
                    json_dict[attr_name] = attr_value
        return json_dict
    
    def reload_from_json(self, json):
        """
        Replaces all attributes of this Student instance with the values from the given JSON dictionary.
        
        The keys of the dictionary must be the names of the public attributes of this class, and the values must
        be the new values for those attributes.
        
        :param json: A dictionary containing the new attribute values for this Student instance.
        """
        for attr_name in json:
            setattr(self, attr_name, json[attr_name])
