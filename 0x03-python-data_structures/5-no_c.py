#!/usr/bin/python3

def no_c(str):
    new_str = ""
    for i in range(len(str)):
        if str[i] == 'C' or str[i] == 'c':
            pass
        else:
            new_str += str[i]
    return new_str
