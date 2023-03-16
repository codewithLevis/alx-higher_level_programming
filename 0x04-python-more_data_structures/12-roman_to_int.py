#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) is not str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    prev_val = 0

    for val in reversed(roman_string):
        curr_val = roman[val]
        if curr_val < prev_val:
            integer -= curr_val
        else:
            integer += curr_val
        prev_val = curr_val

    return integer
