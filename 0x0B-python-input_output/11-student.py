#!/usr/bin/python3
"""Class that defines Student"""


class Student:
    """Initialize student with public variables"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """turns an instance of class student to a json object"""
        if isinstance(attrs, list)\
                and all(isinstance(attr, str) for attr in attrs):
            selected = {k: v for k, v in self.__dict__.items() if k in attrs}
            return selected
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for k, v in json.items():
            self.__setattr__(k, v)
