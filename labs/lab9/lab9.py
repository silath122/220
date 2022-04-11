
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

# True or False think of it like the name of the function is the question and True or False is yes or no if you keep
def is_legal(board, position):
    position = position - 1
    if position < 0 or position > 8 or board[position] == 'x' or board[position] == 'o':
        return False
    else:
        return True

def fill_spot(board, position, character):
    character = character.strip().lower()
    board[position - 1] = character


def winning_game(board):
    for i in range(0, 8, 3):
        if board[i] == board[i+1] == board[i+2]: # rows go up by 1
            return True
    for i in range(0, 3, 1):
        if board[i] == board[i+3] == board[i+6]: # columns go up by 3
            return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    return False

def game_over(board):
    tie = True
    for i in range(9):
        if board[i] != 'x' and board[i] != 'o':
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

    character = 'x'
    playing = True
    while playing:
        while game_over(board) != True:
            for i in range(9):
                print_board(board)
                print("{}'s, choose a position: ".format(character))
                position = int(input(""))
                while is_legal(board, position) != True:
                    print("{}'s, choose a position: ".format(character))
                    position = int(input(""))
                fill_spot(board, position, character)

                if (winning_game(board)):
                    print_board(board)
                    print("Player", get_winner(board), "won!")
                elif (game_over(board)):
                    print_board(board)
                    print("Tie!")

                if character == 'x':
                    character = 'o'
                else:
                    character = 'x'
        cont = input("Would you like to continue playing: ")
        if cont[0] != 'y':
            playing = False
        board = build_board()





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
