#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)

    print("Result of addition: {}".format(addition_result))
    print("Result of subtraction: {}".format(subtraction_result))
    print("Result of multiplication: {}".format(multiplication_result))
    print("Result of division: {}".format(division_result))
