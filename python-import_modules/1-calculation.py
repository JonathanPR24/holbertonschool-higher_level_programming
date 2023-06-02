#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    multiplication_result = mul(a, b)
    division_result = div(a, b)

    print(f"Result of addition: {addition_result}")
    print(f"Result of subtraction: {subtraction_result}")
    print(f"Result of multiplication: {multiplication_result}")
    print(f"Result of division: {division_result}")

