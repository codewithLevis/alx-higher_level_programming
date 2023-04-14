#!/usr/bin/python3

"""Class that defines Student"""
class Student:
  """Initialize student with public variables"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
      """turns an instance of class student to a json object"""
        dictionary = {}
        for attr_name in dir(self):
            attr_value = getattr(self, attr_name)
            if isinstance(attr_value, (str, int)):
                dictionary[attr_name] = attr_value
        return (dictionary)
