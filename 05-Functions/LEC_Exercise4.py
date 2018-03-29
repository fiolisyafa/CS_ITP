import math


def func():
    try:
        return math.factorial(int(input()))
    except ValueError:
        return None

print(func())
