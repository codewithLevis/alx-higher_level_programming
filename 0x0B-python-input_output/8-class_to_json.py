#!/usr/bin/python3
""" function that returns the dictionary description with simple data structure 
(list, dictionary, string, integer and boolean) for JSON serialization of an object
"""

def class_to_json(obj):
	dictionary = {}
	obj_attributes = dir(obj)
	"""Iterate over object attributes"""
	for attr_name in obj_attributes:
		attr_value = getattr(obj, attr_name)
		"""Check if object is serilizable and add to the dictionary"""
		if isinstance(att_value, (list, dict, str, int, bool)):
			dictionary[attr_name] = attr_value
	return (dictionary)			
