from math import sqrt


def hypotenuse(a, b):
    try:
        return sqrt(a**2 + b**2)
    except TypeError:
        return None

print(hypotenuse("6", "7")) # two strings
print(hypotenuse(6, 7)) # two numbers
print(hypotenuse(6, "8")) # one number and one string
