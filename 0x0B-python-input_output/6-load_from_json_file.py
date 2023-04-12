#!/usr/bin/python3
import json

def load_from_json_file(filename):
  """creates an object from a Json file"""
  with open(filename, "r") as file:
    
    object = json.load(file)
    return (object)
