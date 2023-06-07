#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the elements present in only one set
    diff_set = set()

    # Iterate over each element in the first set
    for element in set_1:
        # Check if the element is not present in the second set
        if element not in set_2:
            # Add the element to the different set
            diff_set.add(element)

    # Iterate over each element in the second set
    for element in set_2:
        # Check if the element is not present in the first set
        if element not in set_1:
            # Add the element to the different set
            diff_set.add(element)

    return diff_set
