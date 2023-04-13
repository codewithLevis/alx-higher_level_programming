#!/usr/bin/python3
"""File and Json"""
import sys
import os
from . import save_to_json_file, load_from_json_file

filename = "add_item.json"
if not os.path.exists(filename):
    with open(filename, 'w') as file:
        file.write('[]')
    
"""Load json data from existing file, convert to python object"""
list = load_from_json_file(filename)

list += sys.argv[1:]

"""saves the updated list to file"""

save_to_json_file(list, filename)
