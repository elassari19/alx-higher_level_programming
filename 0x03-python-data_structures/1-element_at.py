#!/usr/bin/python3

def element_at(arr, index):
    if index < 0 or index > len(arr) - 1:
        return None
    else:
        return arr[index]
