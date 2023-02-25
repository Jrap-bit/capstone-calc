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

print (add(1, 2, 3, 4, 5))
print (divide(1, 2))



