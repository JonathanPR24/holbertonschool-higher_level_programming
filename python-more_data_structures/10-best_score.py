#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Initialize variables to keep track of the maximum score and its corresponding key
    max_score = float('-inf')
    max_key = None

    # Iterate over each key-value pair in the dictionary
    for key, value in a_dictionary.items():
        # Check if the value is greater than the current maximum score
        if value > max_score:
            # Update the maximum score and its corresponding key
            max_score = value
            max_key = key

    return max_key
