#!/usr/bin/python3

def magic_calculation(a, b):
    respnse = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            respnse += (a ** b) / i
        except Exception:
            respnse = b + a
            break
    return respnse
