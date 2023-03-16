#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list
    replaced = [idx if idx != search else replace for idx in my_list]
    return replaced
