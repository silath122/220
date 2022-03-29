# strings - sequences of characters
    # examples: "", '', "hello, world!"
    # lists - sequences of objects
    # examples: [] elements inside, ["Paul","George","John","Ringo"], [3, 1, 4, 1, 5, 9],
    # [3, "Monday", 4, "Tuesday"]

    # b = ["Paul", "George", "John", "Ringo"]  #--> type(b) - list
    # a = "hello, world!" - strings
    # len(a) --> 13 (bc it's 13 characters) - concatenation (put things together)
    # len(b) --> 4 (bc it's 4 elements)
    # concatenation --> "hello" + " " + "world" = "hello world"
    # c = "hello" + "world"
    # print(c)
    # helloworld
    # e = "Good morning"
    # d = a + c
    # print(d) # hello, world! Good morning

    # Concatenation /w lists
    # c = b + ["Monday", "Tuesday", "Wednesday"]
    # print(c)
    # ["P", "G", "J", "R", "Monday", "Tuesday", "Wednesday"]
    # c = "hi" * 2 # "hihi"
    # type(c) --> produce a string
    # c = b * 2
    # type(c) --> produce list

    a = "hello, world"
    for l in a:
        print(l)    # print each letter horizontally

    b = ["Paul", "George", "John", "Ringo"]
    for name in b:
        print(name)

    # Indexing - position of list or strings
    # a = [hello, world!"]
    #      0123456789101112
    # b = ["Paul", "George", "John", "Ringo"]
    #        0        1         2       3
    # len(b) - 1
    # a[7]
    # <string>[<int>] - for any string use the square brackets and use the index for every integer
    # print(c) #w
    # type(c) #<str>
    # Ex: d = "Monday"[2]
    # print(d) #n
    # Ex: j = "Monday"[-1]
    # print(j) #y
    # a[-1] #y
    # Ex: b = ["Paul", "George", "John", "Ringo"]
    # name = b[-1] --> Ringo
    # b[-1] = b[len(b) - 1] -- 4 - 3 = 3 = Ringo

    # Substring a group of characters withing a string_
    # access this by slicing
    # syntax for any string --> <string>[<int>: <int>: <int>] - start: stop: step
    # c = a[1: 4]
    # print(c) # ell
    # c = a[1: 8: 2]
    # print(c) # el,w
    # a[:5] # hello
    # a[7:] # world!
    # a[12: 6: -1] #!dlrow
    # a[12:: -1] = a[::-1] # go from the end to the beginning

    # Sublist (A group of elements within elements)
    # access this by slicing (pull multiple elements out)
    # <list>[<int>:<int>:<int>] #start: stop: step
    # c = b[1:3]
    # b[1:2] ["George"] --> b[1] "George"

    # slicing example
    # days = ["mon", "tues", "wed", "thurs", "fri"]
    # type(days[1: 4])
    # list
    # ["tues", "wed", "thurs"]
    # what will these produce?
    # a) days [1: 2]
    # ["tues"] <- list
    # b) days[1]
    # "tues" <- string

    def user_names():
        # enter first name / enter last name / output: user name (first letter first name, first 7 letters last name)
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        # indexing because you need one elements of the string, not multiple (slicing)
        first_letter = first_name[0]
        # slicing because we need all elements of the string, not one (indexing)
        last_seven = last_name[0: 7]
        print("username: "+ first_letter + last_seven)
    user_names()

    def get_month():
        # input: enter month output: what month it is
        # can't use a list, has to be strings, every month is three letters
        months = "janfebmaraprmayjunjulaugsepoctnovdec"
        month_num = eval(input("enter a month: "))
        start_index = month_num * 3 - 3
        stop_index = start_index + 3
        month = months[start_index: stop_index]
        print("That is ", month)
    get_month()

# to initialize a list
    # months = ["January", "February"]
# The code below do not add together since they're different data type
    # months = months + "March"
    # Instead of the following to add to list
    # months = months + ["March", "April"]
# append() adds anything to the list
    # months.append("May")------ you can not append multiple things into a list
# There might be cases when you want to start with an empty list
    # numbers = []
    # for i in range(10):
        # number = eval(input("Enter number: "))
        # numbers.append(number)
# String methods
# the function below makes everything in the string uppercase
# .upper()
# the method below makes everything in the string lowercase
# .lower()
# the method below capitalize the first word of the sentence
# .capitalize()
# this will capitalize the first later of each word
# .title()
# the method below counts the amount of times a word/letters (individually as well) appears in a sentence
# .count()
# the method below finds the index value of a letter/word/sentence
# .find() --- searches from left to right
# .rfind() --- searches from right to left
# the method below replaces strings with another string or words, the first parameter is the word to be replaced, and
# the second parameter is the second that will replace it
# .replace()
# Every element in a list is separated by the factor placed before .join
# .join()

#
def encode():
    word = input("Enter a word: ")
    output = []
    for letter in word:
        output.append(str(ord(letter))) # don't want a space at the end of the last letters code
        print(" ".join(output))
encode()
    word = input("Enter a word: ")
    word_split = word.split(" ")
    for letter in word:
        print(ord(letter), end=" ")
encode()
def decode():
    numbers = input("Enter unicode string: ")
    num_list = numbers.split(" ")  # split string into list ["65", "67", "69"]
    output = " "
    for num in num_list:
        output = output + chr(eval(num))
    print(output)
decode()
# 65 67 69 --> ACE

# .format() - allows you to submit variables into strings
# name = input("Siah)
# "My name is {} ".format(name) <-- the name goes where the curly brackets are placed
# "My name is {} and I am {} years old".format('Siah','20')
# 'My name is Siah and I am 20 years old'
# "My name is {1} and I am {0} years old".format('Siah','20') <-- you can put parameters instead of space so
# My name is 20 and I am Siah years old

# fill, align, and width

# width example:
# "My name is {0:10} and I am {1} years old".format('Eric','7'}
# 'My name is Eric        and I am 7 years old.

# align example:
# "My name is {0:>10} and I am {1:^10} years old".format('Eric','7'} (eric aligns to the right and 7 aligns to the middle
# "My name is           Eric and I am      7     years old"

# money example
# dollar = 12
# cents = 7
# print("I have ${}.{}".format(dollar,cents))
# I have $12.7
# print("I have ${}.{:0>2}".format(dollar, cents))
# I have $12.07

# fill example
# money = 17.70
# print("I have ${:.2f}".format(money))
# I have $17.70

# file

# open(<filename>, <mode>) -- "r" "w"
# my_file = open("data.txt", "r")
my_ch3 = open('ch3.html', 'r')
# 3 methods to read the file: .read(), .readline(), .readlines()

# ch3 = my_ch3.read() -- will return a single string that is the entire contents of the file

# line = my_ch3.readline() -- will return a string, but one line of the file * note at the end of this string
# is going to be a new line character --> \n

# lines = my_ch3.readlines() -- It's going to return a list of strings that is the entire contents of the file
# each element in the string is a new line \n

# ch3 = my_ch3.read()
# ch3 = ch3.replace('e', '$') -- replaces every e with a dollar sign

# do the bellow with poem.txt downloaded

def print_file_lines():
    my_git = open('.getkeep', 'r')
    for i in range(5):
        line = my_git.readline()
        print(line, end='')

print_file_lines()

def print_file_liness():
    my_git = open('.getkeep', 'r')
    for i in range(5):
        line = my_git.readline()
        print(line[:-1])

def print_lines():
    my_git = open('.getkeep', 'r')
    for line in my_git.readlines():
        print(line)

# writing files, use w instead of r
my_output = open('output.txt', 'w')
print("hello, world!", file=my_output)
# creates new file
# or
print('poem.txt', file=my_output) # prints into file





