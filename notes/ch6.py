# Chapter 6: Functions -- 02/21/22

# review:
# def my_function(): -- meaning define my_function
# my_function() -- calling, executing, and evoking a function
# functions: used to reduce code, and avoid duplicate code

import math
from graphics import Point

# sing('George', 'Birthday') -- functions need to be defined before being executed

def happy(holiday):
    print("Happy {} to you".format(holiday))

def sing(holiday, name):     # variable called name that will be accessible within the function
    x = 3  # local to this function only -- local scope
    happy(holiday)
    happy(holiday)
    print("Happy {} dear {}!".format(holiday, name))
    happy(holiday)
# sing("Sweet Sixteen", "Lindsay") # arguements: values being passed to a function -- Lindsay & Sweet Sixteen
# print()
# sing("Birthday", "George")  # do the function twice, same function twice, different names

# 1. execute bad paramater
# 2. name = Lindsay & holiday - 'Sweet Sixteen'
# 3. execute the body
# 4. return back to the function calling

# def <name>(<parameter>):
#     <body>

# () -- parameters help us generalise the function ex: math.sqrt9() vs math.sqrt(9)

# Variable Scope -- what variables have, where and when it is accessible to the program
# ex: name is limited to everything that is within the function body and parameters - the body of the func

x = math.pow(4, 3)  # order of parameters matters
# print(x)

def square(num):
    x = num * num # specific operations require integers or float or strings - this takes integers
    return x
    # to get the function outside the body use return <variable>

three_squared = square(3)
# print(three_squared)

# sphere_area(radius: float) -- provides radius, returns float

# def distance(p1, p2):
    # x1 = p1.getX()
   #  y1 = p1.getY()
   #  x2 = p2.getX()
   #  y2 = p2.getY()
   #  d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))  # if there isn't a return statement - output: None
    # return d
# p1 = Point(2, 3)
# p2 = Point(100, 200)
# my_distance_2 = distance(p1, p2)
# print(d)


# or make it all one line
# def distance_2(p1, p2):
    # return math.sqrt(math.pow(p2.getX() - p1.getX(), 2) + math.pow(p2.getY() - p1.getY(), 2))

point_a = Point(2, 3)
point_b = Point(100, 200)
# my_distance = distance(point_a, point_b)

# sum_diff(num_1: int, num_2: int) -> sum: int, diff: int

def sum_diff(x, y):
    sum_val = x + y
    diff_val = x - y
    return sum_val, diff_val

my_sum, my_diff = sum_diff(10, 7)
print(my_sum)

def get_discount(price, sale):
    # 100, 20% --> .20 --> $80
    price = price * (1 - sale)
    print(price)


price = 100
get_discount(price, .20)
print(price)

def change_point(p, x, y):
    p.move(x, y)

my_point = Point(2, 3)
change_point(my_point, 100, 200)
print(my_point.getX(), my_point.getY())