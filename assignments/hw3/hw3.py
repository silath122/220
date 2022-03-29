"""
Name: <Siah Thomas>
<hw3>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>

"""

def average():
    avg = eval(input("How many grades will you enter? "))
    j = 0
    for i in range(avg):
        temp = eval(input("Enter grade: "))
        j = j + temp
        ms = j / avg
    print("The average is ", ms)

def tip_jar():
    total = 0
    for i in range(5):
        ask = eval(input("How much would you like to donate? "))
        total = total + ask
    print("total tips: ", round(total, 2))

def newton():
    x = eval(input("What number do you want to square root? "))
    times = eval(input("How many times should we improve the approximation? "))
    j = 1
    for i in range(1, times + 1):
        j = 0.5 * (j + (x / j))
        final = j
        print("The square root is approximately ", final)

def sequence():
    terms = eval(input("How many terms would you like? "))
    for i in range(1, terms + 1, 2):
        i = i % 2
        for j in range(1, terms + 1, 2):
            print(i % j, end=" ")


# mod = % for repeating numbers
# for i in range(0, 2):
# print(i% + 1, end=" ")

# days = ["mon", "tues", "wed", "thurs", "fri"]
# for i in range(100):
    # print(days[i%5])
# [i%2] 0, 1 -> [i%3] 0, 1, 2 ->
def pi():
    pass


if __name__ == '__main__':
    pass