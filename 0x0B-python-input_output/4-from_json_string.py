#!/usr/bin/python3
"""File and Json"""
import json


def from_json_string(my_str):
    """Converts a JSON data to a python object"""
    return (json.loads(my_str))
