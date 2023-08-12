#!/usr/bin/python3

def replace_in_list(arr, idx, ele):
    if idx < 0 or idx > len(arr) - 1:
        return arr
    else:
        arr[idx] = ele
        return arr
