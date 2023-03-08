#!/usr/bin/python3
c = 122
while c > 96:
    if c % 2 == 1:
        i = c - 32
    else:
        i = c
    print("{}".format(chr(i)), end="")
    c -= 1
