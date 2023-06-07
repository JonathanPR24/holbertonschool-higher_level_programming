#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    multiplied_dictionary = {}

    # Iterate over each key-value pair in the original dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and store it in the new dictionary
        multiplied_dictionary[key] = value * 2

    return multiplied_dictionary
