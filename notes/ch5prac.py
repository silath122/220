
def username_maker():
    print("This program generate computer usernames. \n")

    # get user's first and last names
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    # concatenate first initial with 7 chars of the last name
    uname = first[0] + last[:7]

    # output username
    print("Your username is: ", uname)

def months_abbrev():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = eval(input("Enter a month number (1-12): "))

    # compute starting position of month n in months
    pos = (n-1) * 3

    # Grab the appropriate slice from months
    monthAbbrev = months[pos:pos+3]
    print("The month abbreviation is", monthAbbrev + ".")

def months_abbrev_list():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
              'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    n = eval(input("Enter a month number (1-12): "))
    print("The month abbreviation is", months[n-1] + ".")

def text2num():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message. \n")

    # get message to encode
    message = input("Please enter a message to encode: ")

    print("\nHere are the Unicode codes: ")

    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")

    print()  # blank line before prompt

def num2text():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build unicode message
    message = ""
    for numStr in inString.split():
        codeNum = eval(numStr)            # convert digits to number
        message = message + chr(codeNum)  # concatentate character to message

    print("\n The decoded message is:", message)
