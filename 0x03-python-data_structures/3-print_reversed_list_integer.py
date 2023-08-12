#!/usr/bin/python3

def print_reversed_list_integer(arr=[]):
    if arr is None:
        return None
    reverse = arr[::-1]
    for i in range(len(reverse)):
        print("{:d}".format(reverse[i]))
