"""
Name: <Siah Thomas>
<hw7>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>

"""


def number_words(in_file_name, out_file_name):
    # open input file and output file
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")

    # accumulate to number the words
    num = 0

    # split the line so it's all a singular string
    for line in infile:
        line_string = line.split()
    # focus on each word of the new line string and use the length of the string to number each word
        for word in line_string:
            num = len(line_string) - (len(line_string) - (num + 1))
            print(num, word[:], file=outfile)
    infile.close()
    outfile.close()

def hourly_wages(in_file_name, out_file_name):
    # open input file and output file
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")

    # split the line it's all a singular string
    for line in infile:
        line_string = line.split()
        new_wage = (float(line_string[2]) + 1.65) * float(line_string[3])
        print(line_string[0], line_string[1], round(new_wage, 2), file=outfile)
    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    isbn = isbn.replace('-', '')
    isbn_sequence = list(isbn)
    num = 11
    sequence_sum = 0
    for each_number in isbn_sequence[:10]:
        num = num - 1
        sequence_sum = sequence_sum + (num * int(each_number))
    print("The checksum is", sequence_sum)
def send_message(file_name, friend_name):
    file_name = open(file_name, "r")
    friend_name = friend_name+'.txt'
    new_file = open(friend_name, "w")

    print(file_name.read(), file=new_file)

    file_name.close()
    new_file.close()


def send_safe_message(file_name, friend_name, key):
    from encryption.py

def send_uncrackable_message(file_name, friend_name, pad_file_name):
    pass


if __name__ == '__main__':
    number_words('pad.txt', 'newfile.txt')
    hourly_wages('hourly_wages.txt', 'new_wages')
    calc_check_sum('0-072-94652-0')
    send_message('friend_message', 'bob')
    send_safe_message('friend_message', 'bob.txt', '7')
