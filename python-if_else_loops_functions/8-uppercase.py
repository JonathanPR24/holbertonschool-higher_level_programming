#!/usr/bin/python3
def uppercase(string):
    for char in string:
        uppercase_char = chr(ord(char) - 32) if ord(char) >= ord('a') and ord(char) <= ord('z') else char
        print("{}".format(uppercase_char), end="")
    print()
