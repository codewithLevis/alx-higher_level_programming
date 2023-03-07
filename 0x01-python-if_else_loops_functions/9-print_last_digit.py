#!/usr/bin/python3
def print_last_digit(number):
    def print_last_digit(number):
    if number < 0:
        last_digit = abs(number) % 10
        last_digit = -last_digit
    else:
        last_digit = number % 10
    print("{}".format(last_digit))
    return (last_digit)
