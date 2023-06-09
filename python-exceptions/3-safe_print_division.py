#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        try:
            print("Inside result: {}".format(result))
        except NameError:
            pass
    return result
