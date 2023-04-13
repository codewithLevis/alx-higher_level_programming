#!/usr/bin/python3
"""Module For MyList"""


class MyList(list):
    '''Inherits from list'''

    def print_sorted(self):
        '''print sorted list in ascending order'''
        print(sorted(self))