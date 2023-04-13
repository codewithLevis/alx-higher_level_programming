#!/usr/bin/python3
"""File and Json"""


def read_file(filename=""):
    """Function that opens, reads and print file content to the console"""
    with open(filename, encoding="utf-8") as f:
        filecontent = f.read()
        print(filecontent, end="")
