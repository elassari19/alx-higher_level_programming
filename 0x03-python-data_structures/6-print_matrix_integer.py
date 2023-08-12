#!/usr/bin/python3

def print_matrix_integer(arr=[[]]):
    if arr is None:
        print("")
    else:
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print("{:d}".format(arr[i][j]), end="")
                if j != len(arr[i]) - 1:
                    print(" ", end="")
            print("")
