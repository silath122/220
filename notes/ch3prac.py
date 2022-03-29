import math
def prob1():
    # calculates the volume and surface area of a sphere
    r = eval(input("Enter the radius of the sphere: "))
    volume = (4/3) * math.pi * (r ** 3)
    area = 4 * math.pi * (r ** 2)
    print("The surface area of the sphere is", area)
    print("The volume of the sphere is", volume)

def prob4():
    # calculates the distance to a lightning strike based on time elapsed between the flash
    # and the sound of thunder. The speed of sound is approximately 1100 ft/sec and 1 mile is 5280 ft
    print("Calculate how far you are to the lightning strike")
    time = eval(input("Enter the time between the flash and the sound of thunder, in seconds: "))
    miles = (time * 1100) / 5280
    print("The distance from the lightning strike is", round(miles,2),"miles.")
def prob11():
    # calculates the sum of the first n natural numbers, where the value of n is provided by the user
    n = eval(input("Enter a natural number: "))
    add = 0
    for i in range(1, n+1):
        add = add + i
    print(add)
def prob12():
    n = eval(input("Enter a natural number: "))
    add = 0
    for i in range(1, n+1):
        add = add + (i ** 3)
    print(add)
def prob13():
    # program to sum a series of numbers entered by the user
    n = eval(input("How many numbers are to be entered? "))
    add = 0
    for i in range(1, n + 1):
        i = eval(input("Enter number: "))
        add = add + i
    print(add)
def prob14():
    # finds the average of a series of numbers entered by the user
    n = eval(input("How many numbers are to be entered? "))
    add = 0
    for i in range(1, n + 1):
        i = eval(input("Enter number: "))
        add = add + i
    avg = add / n
    print("The average of the series of numbers is", float(avg))
def prob15():
    n = eval(input("Enter the number of terms to sum: "))
    add = 0
    sub = 0

    for i in range(0, n):
        i = (i + (i + 1))
        new_num = 4 / i

prob15()

def newton():
    number_square = eval(input("What number do you want to square root? "))
    number_improve = eval(input("How many times should we improve the approximation? "))
    sum = 4
    for approx_times in range(1, number_improve + 1):
        sum = (sum + (number_square / sum)) / 2
    print("The square root is approximately ", sum)

