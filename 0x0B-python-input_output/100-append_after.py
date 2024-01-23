#!/usr/bin/python3
"""
Module for append after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file
    after each line containing a specific string (see example)
    """
    insertion_indices = []
    lines = []

    if filename:
        with open(filename, "r") as file:
            lines = file.readlines()

            for _ in range(len(lines)):
                if search_string in lines[_]:
                    insertion_indices.append(_)

            count = 0  # count for previous insertions

            for _ in insertion_indices:
                lines.insert(_ + 1 + count, new_string)
                count += 1

            file.close()
        with open(filename, "w") as file:
            file.writelines(lines)
            file.close()
