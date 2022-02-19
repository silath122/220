"""
Name: <Siah Thomas>
<hw5>.py

Problem: <These programs computes the last and first name, the company of a website, initials, multiple initials,
multiple names of students, specific letters from sentence, the average length of sentences, and pig latin>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>

"""


def name_reverse():
    name = input("Enter a name (first last): ")
    name_list = name.split()
    print(name_list[1]+", "+name_list[0])

def company_name():
    domain = input("Enter a domain: ")
    domains = domain[4:-4]
    print(domains)

def initials():
    num_students = eval(input("How many students are in the class? "))
    for i in range(1, num_students + 1):
        print("What is the name of student", i, end="?")
        name = input()
        first_name, last_name = name.split()
        print(first_name[0]+last_name[0])
def names():
    names = input("Enter a list of names: ")
    names_list = names.split(",")
    # split each full name and use /t to make everything align together
    for full_name in names_list:
        first_name, last_name = full_name.split()
        print(first_name[0]+last_name[0], end="\t")

def thirds():
    num_sentence = eval(input("Enter the number of sentences: "))
    for statement in range(1, num_sentence + 1):
        print("Enter sentence", statement, end=": ")
        sentence = input()
        output = sentence[::3]
        print(output, end="\n")

def word_average():
    sentence = input("Enter a sentence: ")
    sentence = sentence.split()
    word_length = []

    for word in sentence:
        word_length.append(len(word))
    average = sum(word_length) / len(word_length)

    print(average)

def pig_latin():
    sentence = input("Enter a sentence to convert to pig latin: ")
    sentence = sentence.split()
    print(sentence)
    for each_word in sentence:
        # move letter to the end of the word and join ay to it
        letters = each_word.split()
        for each_letter in letters:
            movement = each_letter[], each_letter[:1]
            print(movement)
# i give up :(
pig_latin()

if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
