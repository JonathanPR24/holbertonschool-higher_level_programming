#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b < 0:
        for _ in range(abs(b)):
            result /= a
    else:
        for _ in range(b):
            result *= a
    return "{:.20f}".format(result)
