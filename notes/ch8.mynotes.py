# indefinite vs definite loops

# definite:
# for <var> in <sequence>:
#               <bodyy>

# indefinite:
# while <condition>:
#   <body>

# example a) while loop that counts from 0 to 10
# i = 0
# while i <= 10:
#   print(i)
# i = i + i

# example b) for loop
# for i in range(11):
#   print(i)

# average2.py - indefinite loop basic example
def average2():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == 'y':
        x = eval(input("Enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more  numbers (yes or no)? ")
    print("\nThe average of the numbers is", sum / count)

# sentinel loops: continues to process data until reaching a special value that signals the end
# average3.py - sentinel loop example - if you type in any number less than 0, it will end the program.
def average3():
    sum = 0.0
    count = 0
    x = eval(input("Enter a number (negative to quit) >> "))
    while x >= 0:    # sentinel portion
        sum = sum + x
        count = count + 1
        x = eval(input("Enter a number (negative to quit) >> "))
    print("\nThe average of the numbers is", sum / count)

# average4.py - no range of numbers, includes positives and negatives
def average4():
    sum = 0.0
    count = 0
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = eval(xStr)
        sum = sum + x
        count = count + 1
    print("\nThe average of the number is ", sum / count)

# file loops
# average5.py - file loop
def average5():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    for line in infile:
        sum + eval(line)
        count = count + 1
    print("\nThe average of the number is", sum / count)

# you can read the lines of a file one at a time by using a sentinel loop !!!!!
# example:
# line = infile.readline()
# while line! = "":
# line = infile.readline()

# average6.py - apply the end-of-file sentinel loop
def average6():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", sum / count)

# Nested loops
# average7.py - a file with numbers on one line seperated by commas
def average7():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        # update sum and count for values in line
        for xStr in line.split(","):
            sum = sum + eval(xStr)
            count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", sum / count)




if __name__ == '__main__':
    average6()