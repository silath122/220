
def birthday_song():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Fred!")
    print("Happy Birthday to you!")

def happy():
    print("Happy Birthday to you!")

def singFred():
    happy()
    happy()
    print("Happy Birthday, dear Fred!")
    happy()

def singLucy():
    happy()
    happy()
    print("Happy Birthday, dear Lucy!")
    happy()

def two_birthdays():
    singLucy()
    print()
    singFred()

def sing(person):
    happy()
    happy()
    print("Happy Birthday, dear", person + "!")
    happy()

def person_birth():
    sing("Lola")
    print()
    sing("Henry")

import math
from graphics import *

# triangle2 program
def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

def triangle():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # draw triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate perimeter
    perim = distance(p1, p2) + distance(p2, p3) + distance (p3, p1)
    message.setText("The perimeter is : {0:0.2f}".format(perim))

    # wait for another click to exit
    win.getMouse()
    win.close()

def sumdiff(x, y):
    sum = x + y
    diff = x - y
    return sum, diff

def num():
    num1, num2 = eval(input("Please enter two numbers (num1, num2) "))
    s, d = sumdiff(num1, num2)
    print("The sum is", s, "\nThe difference is", d)

def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    return newBalance

def test_interest():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print(amount)
