#!/usr/bin/python3
def uppercase(string):
    uppercase_string = ""
    for char in string:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        uppercase_string += uppercase_char
    print(uppercase_string)
