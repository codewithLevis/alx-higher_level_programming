#!/usr/bin/python3
"""
Module printing a string and the manner
of printing is affected by three ".?:" characters
"""


def text_indentation(txt):
    """  function that prints a text with 2 new lines  """
    if not isinstance(txt, str):
        raise TypeError("txt must be a string")

    i = 0
    while i < len(txt) and txt[i] == ' ':
        i += 1

    while i < len(txt):
        print(txt[i], end="")
        if txt[i] == "\n" or txt[i] in ".?:":
            if txt[i] in ".?:":
                print("\n")
            i += 1
            while i < len(txt) and txt[i] == ' ':
                i += 1
            continue
        i += 1
