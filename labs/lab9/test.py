while game_over(board) != True:  # true or false?
    player = 'x'
    if player == 'x':
        player = 'o'
        position = eval(input("x's, choose a position: "))
        if is_legal(board, position) == True:  # true or false?
            fill_spot(board, position, player)
        else:
            return is_legal(board, position)
    else:
        player = 'o'
        position = eval(input("o's, choose a position: "))
        if is_legal(board, position) == True:
            fill_spot(board, position, player)
        else:
            return is_legal(board, position)
if get_winner(board) == 'o' or 'x':
    print("{}'s won!".format(get_winner(board)))
else:
    print("tie")
