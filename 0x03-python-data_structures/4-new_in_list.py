#!/usr/bin/python3

def new_in_list(arr, idx, ele):
    if idx < 0 or idx > len(arr) - 1:
        return arr
    else:
        new_arr = my_list[:]
        new_arr[idx] = ele
        return new_arr
