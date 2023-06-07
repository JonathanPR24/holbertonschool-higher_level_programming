#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Iterate over each element in the input list
    for element in my_list:
        # Check if the element is an integer
        if isinstance(element, int):
            # Add the integer to the set of unique integers
            unique_integers.add(element)

    # Compute the sum of unique integers
    total_sum = sum(unique_integers)

    return total_sum
