
def convert():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

def convert2():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    # print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be Careful!")
    if fahrenheit < 30:
        print("Brrrrr. Be sure to dress warmly!")

# < less than
# > greater than
# == equal to
# =< less than or equal to
# >= greater than or equal to
# != not equal

import math

def quadratic():
    print("This program finds the real solutions to a quadratic\n")

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / 2 * a
    root2 = (-b - discRoot) / 2 * a

    print("\nThe solutions are:", root1, root2)

# ValueError: math domain error when it can't be computed

def quadratic2():
    print("This program finds the real solutions to a quadratic\n")

    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    discrim = b * b - 4 * a * c
    if discrim >= 0:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / 2 * a
        root2 = (-b - discRoot) / 2 * a
        print("\nThe solutions are:", root1, root2)

def quadratic3():
    print("This program finds the real solutions to a quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real roots!")
    else:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / 2 * a
        root2 = (-b - discRoot) / 2 * a
        print("\nThe solutions are:", root1, root2)

# double root
def quadratic4():
    print("This program finds the real solutions to a quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))

    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real roots!")
    elif discrim == 0:
        root = -b / 2 * a
        print("\n There is a double root at", root)
    else:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / 2 * a
        root2 = (-b - discRoot) / 2 * a
        print("\nThe solutions are:", root1, root2)

# catch errors of math.sqrt
def quadratic5():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / 2 * a
        root2 = (-b - discRoot) / 2 * a
        print("\nThe solutions are:", root1, root2)
    except ValueError as exc0bj:
        if str(exc0bj) == "math domain error":
            print("No Real Roots")
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError:
        print("\nYou didn't give me the right number of coefficients.")
    except TypeError:
        print("\nYour inputs were not all numbers.")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong, sorry!")


# finds the maximum of a series of numbers
def maxn():
    n = eval(input("How many numbers are there? "))

    # set max to be the first value
    max = eval(input("Enter a number >> "))

    # Now compare the n-1 sucessive values
    for i in range(n-1):
        x = eval(input("Enter a number >> "))
        if x > max:
            max = x
    print("The largest value is", max)


if __name__ == '__main__':
    convert2()
    quadratic3()