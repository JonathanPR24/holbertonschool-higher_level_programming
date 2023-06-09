#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        try:
            print("Inside result: {}".format(result))
            print("{} / {} = {}".format(a, b, result))
        except NameError:
            pass
    return result
