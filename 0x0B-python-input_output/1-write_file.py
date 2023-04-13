#!/usr/bin/python3
"""File and Json"""


def write_file(filename="", text=""):
    '''Function writes a string to a text file 
    and returns the number of characters written'''
    with open(filename, "w", encoding='utf8') as file:
        try:
            file.write(text)
            return len(text)
        except Exception as e:
            print("Error writing to file {}: {}".format(filename, e))
            raise e
