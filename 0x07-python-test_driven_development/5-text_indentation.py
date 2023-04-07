#!/usr/bin/python3
"""
Module printing a string and the manner
of printing is affected by three ".?:" characters
"""
 function that prints a text with 2 new lines after each of these characters: ., ? and :

def text_indentation(text):
    """  function that prints a text with 2 new lines  """

    if type(text) is not str:
        raise TypeError("text must be a string")

    mod_text = text[:]

    for char in ".?:":
        parsed_t = s.split(d)
        s = ""
        for i in parsed_t:
            i = i.strip(" ")
            mod_text = i + char if mod_text is "" else mod_text + "\n\n" + i + char

    print(mod_text[:-3], end="")
