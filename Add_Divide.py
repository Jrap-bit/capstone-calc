def add(*args):
    total = 0
    for num in args:
        total += num
    return total


def divide(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is undefined")
