import math

def convert():
    # convert celsius temps to fahrenheit
    # this version issues heat and cold warnings
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees fahrenheit.")

    # Print warnings for extreme temps, ignores if it doesn't agree with statement
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrrr. Be sure to dress warmly!")


# Boolean expressions --> bool < bool
# < - less then
# <= - less than or equal to
# == - equal to
# >= greater than or equal to
# > greater than
# != not equal to



# 03/02/22

# nested if statement
def quadratic(a, b, c):
    disc = b * b - 4 * a * c
    if disc < 0:
        print('no real roots')
    # else if then else : elif to avoid nesting
    # what ever the code see first it runs it and skips everything
    elif disc > 1:
        print('on')
    elif disc > 9:
        print('9')
    # if starts a new problem all over again, both if are 2 different statements
    # can't have an else before an elif
    if disc > 10:
        print('10')
    elif disc == 0:
        sqrt_discr = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        print('double root:', root_1)
    else:
        sqrt_discr = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        root_2 = (-b - sqrt_discr) / denom
        print('root  1:', root_1, 'root 2:', root_2)


# can test multiple things using and, and is a logical operator
# bool and bool --> will return a bool
# example: x = 9 - check if x > 3 and x < 10
# truth table with and using a p and q
# x = 9 problem will evaluate to True, if true run the body

# find the maximum value of three inputs
def max(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c
def mex(a, b, c):
    if a >= b:
        if a >= c:
            return a
        else:
            return c
    if b >= c:
        return b
    return c
def tex(a, b, c, d):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    if d > max_value:
        max_value = d
    return max_value
def lax(values):
    max_value = values[0]
    for value in values:
        if value >= max_value:
            max_value = value
        return max_value

# built in functions max(1, 2, 3) --> 3
# or max([1, 3, 5, 3, 1]) --> 5

# Errors

# ex: sqrt_discr = math.sqrt(disc)
# ValueError: math domain error
# when an error occurs its called and error object, different types of errors

# exceptions are thrown!
# We know the code might has an error but we want to "try:"
# example: enter 3 4 1 instead of 3, 4, 1 --> syntax error
# have to define for specific errors

def quadratic_2(a, b, c):
    try:
        disc = b * b - 4 * a * c
        sqrt_discr = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        root_2 = (-b + sqrt_discr) / denom
        print('root 1:', root_1, 'root 2:', root_2)
    # if there is an error then except -- define specifc error
    except:
        print('no real roots')

# user input: could you get many errors and same results?
def quadratic_3():
    try:
        a, b, c = eval(input('enter coefficients: '))
        disc = b * b - 4 * a * c
        sqrt_discr = math.sqrt(disc)
        denom = 2 * a
        root_1 = (-b + sqrt_discr) / denom
        root_2 = (-b + sqrt_discr) / denom
        print('root 1:', root_1, 'root 2:', root_2)
    # if there is an error then except
    except ValueError as e:
        # print(e) - prints type of error
        # when the roots are real or when you dont enter enough values
        if str(e) == 'math domain error':
            print('no real roots')
        else:
            print('bad input: did you enter 3 values?')
    except SyntaxError:
        print('bad input: did you use commas?')
    # using letters instead of numbers
    except NameError:
        print('bad input: did you type all numbers?')
    except:
        print('an error occured. no idea why')
if __name__ == '__main__':
    max(3, 5, 10)
    lax([-1, -7, -2, -4])
    quadratic_2(1, 1, 2)
    quadratic_3()



