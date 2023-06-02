#!/usr/bin/python3
#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    a = 10
    b = 5

    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print(f"{a} + {b} = {add_result}")
    print(f"{a} - {b} = {sub_result}")
    print(f"{a} * {b} = {mul_result}")
    print(f"{a} / {b} = {div_result}")
