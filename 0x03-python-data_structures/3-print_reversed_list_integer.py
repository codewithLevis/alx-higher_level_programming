#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    if my_list != None:
        i = -1
        while i != -(length + 1):
            print('{:d}'.format(my_list[i]))
            i = i - 1
