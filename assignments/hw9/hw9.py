from random import randint
import words as words


def get_words(file_name):
    words_file = open(file_name,"r")
    new_words = words_file.readlines()
    words = []
    for word in new_words:
        new_word = word.replace("\n", "")
        words.append(new_word)
    return words

def get_random_word(words):
    secret_word = words[randint(0, 999)]
    # not sure if this will work bc get_random_word('words') thinks it's computing
    # 'words' as a list not the actual list computed previously of all the words in a list
    return secret_word

def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False

def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False

def make_new_secret_word(secret_word):
    secret_str = []
    secret_word = secret_word.split()

    # word will look like "t_i_m_e_"
    for secret_letter in secret_word:
        secret_str = secret_str + secret_letter.append('_')
    new_secret_word = "".join(secret_str)
    return new_secret_word

def make_hidden_secret(new_secret_word, secret_word, guesses):

    # when letter is found the word will look like "tti_m_e_" when the t is found
    for each_guess in guesses:
        if new_secret_word.find(each_guess) == True:
            secret_word.replace(secret_word[(secret_word.find(each_guess) + 1)], each_guess, 1)
        elif new_secret_word.find(each_guess) == False:
            return False

    # this will make the guessed version look like "t___"
    guessed = []
    for i in range(0, len(secret_word) - 1, 2):
        guessed = guessed + list(secret_word[i])
    return guessed


def won(guessed):
    if guessed.find('_') == False:
        return True
    else:
        return False

def play_graphics(secret_word):
    pass


def play_command_line(secret_word, new_secret_word):
    get_words('words.txt')
    num_guess = 6
    guesses = []
    make_new_secret_word(secret_word)
    while num_guess != 0:
        print("already guess: ", guesses)
        print("guesses remaining: ", num_guess)
        letter = input("guess a letter: ")
        print(new_secret_word)
        if letter_in_secret_word(letter, secret_word):
            if already_guessed(letter, guesses):
                guesses.append(letter) and (num_guess - 1)
                make_hidden_secret(new_secret_word, secret_word, guesses)
            else:
                return False
        else:
            if won(guessed):
                print("won!")
                print(secret_word)
            else:
                if

    print(secret_word)



if __name__ == '__main__':
    play_command_line('secret_word', 'new_secret_word')
    # play_command_line(secret_word)
    # play_graphics(secret_word)
