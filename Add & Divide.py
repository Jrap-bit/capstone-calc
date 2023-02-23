def add(*args):
    total = 0
    for num in args:
        total += num
    return total


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b