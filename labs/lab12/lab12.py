from random import randint


def find_and_remove(list, value):
    i = 0
    while i < len(list):
        if value == list[i]:
            list.pop(i)
            list.insert(i, 'siah')
        i = i + 1


def good_input():
    user_num = eval(input("The range is between 1 and 10, Input within range: "))
    while user_num < 1 or user_num > 10:
        if user_num < 1:
            print("Input was too low")
        else:
            print("Input was too high")
        user_num = eval(input("Try again: "))
    return user_num

def num_digits():
    user_input = eval(input("Enter a positive number (enter 0 or negative to end program): "))
    while user_input > 0:
        count = 0

        while user_input > 0:
            user_input = user_input // 10
            count = count + 1
        print("The number has", count, "digits")
        user_input = eval(input("Enter a positive number: "))

def hi_lo_game():
    rand_num = randint(1, 100)
    guesses = 7

    user_guess = eval(input("Guess number: "))
    guesses = guesses - 1

    while guesses != 0 and guesses != -1:
        if user_guess > rand_num:
            user_guess = eval(input("Number too high, guess again: "))
            guesses = guesses - 1
        elif user_guess < rand_num:
            user_guess = eval(input("Number too low, guess again: "))
            guesses = guesses - 1

        elif user_guess == rand_num:
            print("You won in", 7 - guesses, "guesses!")
            guesses = -1
    if guesses == 0:
        print("Sorry, you lose. The number was", rand_num)

if __name__ == '__main__':
    list = ['mouse', 'dog', '20', '25', '13', 'blue', 'red']
    print(list)
    find_and_remove(list, "red")
    print(list)