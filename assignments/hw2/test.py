from tests.hw2 import test

import math

# Input: lower and upper ranges Output: sum of the squares
# list of the rang
# 4 * 4 * 4 specify how many times you multiply by the base
# multiply it by the specific number of times

def power():
    print("Calculate the power of numbers.")
    print()
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    j = 1
    for i in range(1, exponent + 1):
        j = j * base
    print(base, "^", exponent, "=", j)
power()







