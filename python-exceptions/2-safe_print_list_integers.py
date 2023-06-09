#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for element in my_list[:x]:
            try:
                if isinstance(element, int):
                    print("{:d}".format(element), end=" ")
                    count += 1
            except ValueError:
                pass
    except (IndexError, TypeError):
        pass

    print()
    return count
