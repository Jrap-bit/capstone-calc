def add(*args):
    total = 0
    for num in args:
        total += num
    return total


def divide(a, b):
    if b == 0:
        print("Can't divide by zero!")
    return a / b

print (add(1, 2, 3, 4, 5))
print (divide(1, 2))