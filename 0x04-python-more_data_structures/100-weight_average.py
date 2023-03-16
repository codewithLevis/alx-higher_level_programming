#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    tot_weight = 0
    value_tot = 0

    for tup in my_list:
        tot_weight += tup[0] * tup[1]
        value_tot += tup[1]

    return tot_weightnum / value_tot
