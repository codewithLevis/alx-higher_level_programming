#!/usr/bin/python3
"""File and Json"""


def write_file(filename="", text=""):
    '''Function writes a string to a text file 
    and returns the number of characters written'''
    with open(filename, "w", encoding='utf8') as file:
        return file.write(text)
