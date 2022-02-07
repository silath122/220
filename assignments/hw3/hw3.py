"""
Name: <Siah Thomas>
<hw3>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>

"""
import math

def average():
    avg = eval(input("How many grades will you enter? "))
    j = 0
    for i in range(avg):
        temp = eval(input("Enter grade: "))
        j = j + temp
        ms = j / avg
    print("The average is ", round(ms, 1))

def tip_jar():
    total = 0
    for i in range(5):
        ask = eval(input("How much would you like to donate? "))
        total = total + ask
    print("total tips: ", round(total, 2))

def newton():
    t = eval(input("What number do you want to square root? "))
    ap = eval(input("How many times should we improve the approximation? "))
    j = 0
    for i in range(ap):
        j = (j + (t / ap)) / 2
    print("The square root is approximately", j)

def sequence():
    pass



def pi():
    pass


if __name__ == '__main__':
    pass