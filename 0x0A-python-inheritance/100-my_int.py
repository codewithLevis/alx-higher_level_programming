#!/usr/bin/python3
"""Module for MyInt subclass"""

class MyInt(int):
    '''Overides the equal method of parent class'''
    def __eq__(self, other):
        return (super().__ne__(other))
    
    def __ne__(self, other):
        '''Overides the  not equal method of parent class'''
        return (super().__eq__(other))