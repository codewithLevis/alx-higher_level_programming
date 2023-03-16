#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary)
    for k in keys:
        print(k + ':', a_dictionary[k])
