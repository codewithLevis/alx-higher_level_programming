#!/usr/bin/python3
"""
class student
"""


class Student:
    """Initialize student attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        the method retrieves all attributes if none is provides. 
        Else it filters the list of attributes to include only
        those that are specified in the attrs list.
        """
         if isinstance(attrs, list):
            for i in attrs:
                if not isinstance(i, str):
                    return self.__dict__
            my_dic = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dic.update({key: value})
            return my_dic
        else:
            return self.__dict__
