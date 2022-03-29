
"""
Name: <Siah Thomas>
<lab9>.py
"""

# list of 9 elements, one for each position on the board - build board
def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if board[position] == 'x' or 'o' and 0 <= position >= 8:
        return False
    else:
        return True

def fill_spot(board, position, character):
    character = character.strip().lower()
    board[position - 1] = character


def winning_game(board):
    for i in range(0, 8, 3):
        if board[i] == board[i+1] == board[i+2]:
            return True
    for i in range(0, 3, 1):
        if board[i] == board[i+1] == board[i+2]:
            return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    return False

def game_over(board):
    tie = True
    for i in range(9):
        if board[i] != 'x' or board[i] != 'o':
            tie = False
        return winning_game(board) or tie


def get_winner(board):
    if winning_game(board):
        xCount = 0
        oCount = 0
        for position in board:
            if position == 'x':
                xCount += 1
            elif position == 'o':
                oCount += 1
        if xCount == oCount:
            return 'o'
        else:
            return 'x'
    else:
        return None


def play(board):
    while game_over(board) != True:
        character = 'x'
        for i in range(9):
            print_board(board)
            print("{}'s, choose a position: ".format(character))
            position = eval(input(""))
            while is_legal(board, position) != True:
                print("{}'s, choose a position: ".format(character))
                position = eval(input(""))
            fill_spot(board, position, character)
            if character == 'x':
                character = 'o'
            else:
                character = 'x'
        print_board(board)




# 2 while loops nested
# outside one is while we're playing again, one game of tic tac toe
# inside is while the game is not over, one persons turn
# for each turn --

# whos turn
# what position, print the board
# within the while loop check if valid, prompt again and again until correct use while loop
# place the position once valid
# that's all you need to

# print winner or tie
# ask if they want to play again
# main function
# start your loop
# in play make sure to reset board, build board gives a fresh board

# each round print the board


def main():
    play(build_board())


# build board
# play with board


if __name__ == '__main__':
    main()
