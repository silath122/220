"""
Name: <Siah Thomas>
<hw2>.py

Problem: <This calculates the sum of all multiples of three, a multiplication table, area of a triangle, sum of squares,
and the power function.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>

"""
import math


def sum_of_threes():
    print("Calculate the sum of all multiples of three with a given number.")
    print()
    upper = eval(input("What is the upper bound? "))
    my_range = list(range(upper, 0, -3))
    three = sum(my_range)
    print("the sum of threes is ", three)


def multiplication_table():
    print(" A multiplication table for numbers 1 to 10.")
    print()
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print("\n")

def triangle_area():
    print("Calculate the area of a triangle.")
    print()
    a = eval(input("Enter the length of side a: "))
    b = eval(input("Enter the length of side b: "))
    c = eval(input("Enter the length of side c: "))
    s = (a + b + c) / 2
    air = (s - a) * (s - b) * (s - c)
    airs = math.sqrt(s * air)
    print("The area is ", airs)

def sum_squares():
    print("Calculate the sum of the squares of the given lower and upper range.")
    print()
    lower = eval(input("Enter the lower range: "))
    upper = eval(input("Enter the upper range: "))
    j = 0
    for i in list(range(lower, upper + 1)):
        j = j + (i * i)
    print(j)

def power():
    print("Calculate the power of numbers.")
    print()
    base = eval(input("Enter the base: "))
    exponent = eval(input("Enter the exponent: "))
    j = 1
    for i in range(1, exponent + 1):
        j = j * base
    print(base, "^", exponent, "=", j)


if __name__ == '__main__':
    pass
