"""
Name: <Siah Thomas>
<hw6>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>

"""


def cash_converter():
    integer = eval(input("Enter an integer:"))
    print("That is ${}.00".format(round(integer, 2)))

def encode():
    message = input("Enter a message:")
    key = eval(input("Enter a key: "))
    code = ""
    for ch in message:
        unicode = ord(ch) + key
        new_message = chr(unicode)
        code = code+new_message
    print(code)


def sphere_area(radius):
    new_rad = float(radius)
    area = 4 * 3.14 * (new_rad * new_rad)
    return area
rad_1 = eval(input("Enter the radius of the sphere: "))
p = sphere_area(rad_1)
print("The surface area of the sphere is", float(p))

def sphere_volume(radius):
    new_rad = float(radius)
    volume = (4 / 3) * 3.14 * (new_rad * new_rad * new_rad)
    return volume
rad_2 = eval(input("Enter the radius of the sphere: "))
q = float(sphere_volume(rad_2))
print("The volume of the sphere is", q)

def sum_n(number):
    new_num = int(number)
    add = 0
    for each_number in range(1, new_num + 1):
        add = add + each_number
    return add
new_num_2 = eval(input("Enter a natural number: "))
r = int(sum_n(new_num_2))
print("The sum of the first natural numbers are", r)

def sum_n_cubes(number):
    new_cube_number = int(number)
    add_2 = 0
    for each_number in range(1, new_cube_number + 1):
        add_2 = add_2 + (each_number * each_number)
    return add_2
new_cube_number_2 = eval(input("Enter a natural number: "))
s = int(sum_n_cubes(new_cube_number_2))
print("The sum of the cubes of the first natural number are", s)

def encode_better():
    # Get message and key from user
    message = input("Enter a message to be encoded: ")
    key = input("Enter a key: ")

    # Convert message and key to uppercase and remove spaces
    message = message.upper().replace("", "")
    key = key.upper().replace("", "")

    # Encoded message
    encoded_message = ""

    # Perform character shift
    for i in range(len(message)):
        letter_value = ord(message[i]) - 65
        shift_amt = ord(key[i % len(key)]) - 65
        new_letter = letter_value + shift_amt
        new_letter = new_letter % 26
        new_letter = new_letter + 65
        new_letter = chr(new_letter)
        encoded_message = encoded_message + new_letter

    print(encoded_message)
if __name__ =='__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
