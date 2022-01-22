"""
Name: <Siah Thomas>
<hw1>.py

Problem: <This program solves the area of a rectangle, the volume of a rectangular solid, the basketball shooting
percentage of a player, the cost of shipping a coffee order, and a conversion from kilometers to miles.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>

"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the length: "))
    area = length * width
    print("Area =", area)

calc_rec_area()

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

calc_volume()

def shooting_percentage():
    total = eval(input("Enter the player's total shots: "))
    shots = eval(input("Enter how many shots the player made: "))
    percentage = (shots / total) * 100.0
    print("Shooting Percentage: "+str(percentage)+"%")

shooting_percentage()

def coffee():
    pounds = eval(input("How many pounds of coffee would you like? "))
    total = (pounds * 10.50) + (pounds * 0.86) + 1.50
    print("You're total is: "+str(total)+"$")

coffee()

def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    miles = round(kilometers / 1.61, 2)
    print("That's", miles, "miles!")

kilometers_to_miles()

if __name__ == '__main__':
    pass
