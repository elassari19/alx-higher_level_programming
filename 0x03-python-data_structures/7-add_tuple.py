#!/usr/bin/python3

def add_tuple(tuple_1=(), tuple_2=()):
    if (len(tuple_1) == 0):
        tuple_1 = (0, 0)
    elif (len(tuple_1) == 1):
        tuple_1 = (tuple_1[0], 0)
    if (len(tuple_2) == 0):
        tuple_2 = (0, 0)
    elif (len(tuple_2) == 1):
        tuple_2 = (tuple_2[0], 0)

    return (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
