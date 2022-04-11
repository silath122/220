# Loops
#1. for --> definite loop
#        for i in [1, 2, 3]:
# if <condition> - it'll run through the condition once
#   <body>

#2. indefinite/conditional loop
# called a while loop - check condition every time you check the body to make sure its still true under the condition
# while <condition>:
#       <body>

def my_first_while():
    for i in range(5):
        print(i, end=' ')
    print('\n{0:-<70}'.format(''))

    i = 0
    # while True: -- will make it continously print forever - update condition within while loop
    while i < 5:
        print(i, end=' ')
        # without sum it'll print 0 infinitely
        # ctrl + c will end a console if it continously goes and won't stop
        i = i + 1

def is_equal(p1, p2): # use a conjunction truth table to see options - and, or, not Boolean operators
    if p1.getX() == p2.getX() and p1.getY() == p2.getY():
        return True
    else:
        return False

def is_game_over(player_one_points, player_two_points): # win at 15
    # or you could doa absolute value and delete the second
    is_over_fifteen = player_one_points >= 15 or player_two_points >= 15
    won_by_two = abs(player_one_points - player_two_points) >= 2
    skunked = player_one_points >= 7 and player_two_points <= 0 or player_two_points >= 7 and player_one_points <= 0
    if is_over_fifteen and won_by_two or skunked:
        return True
    return False


# def Morgan_one(a,b):
    # return not (a and b) == (not a or not b)
def whoops():
    ans = input('do you want to transfer all of your money out of your bank account? ')
    if ans == 'y' or 'yes':
       print('ok, transferring..')
    else:
        print('good idea.')

def ice_cream():
    ans = input('what is your favorite ice-cream? [vanilla]')
    favorite = ans or 'vanilla'
    # if ans:
        # favorite = ans
    # else:
        # favorite = 'vanilla'
    print('your favorite is {}'.format(favorite))
# Short circuit
# x and y - if x is false, return x. Otherwise, return y
# x or y - if x is true, return x. Otherwise, return y
# not x - if x is false, return True. Otherwise, return False.

def average():
    count = eval(input('How many numbers do you have? '))
    acc = 0
    for i in range(count):
        num = eval(input('enter number>> '))
        acc = acc + num
    print('average is {}.'.format(acc / count))

def while_average():
    count = eval(input('How many numbers do you have? '))
    acc = 0
    i = 0
    while i < count:
        num = eval(input('enter number>> '))
        acc = acc + num
        i = i + 1
    print('average is {}.'.format(acc / count))

def average_interactive():
    acc = 0
    count = 0
    ans = 'y'
    while ans[0] == 'y'
        num = eval(input('enter number>> '))
        acc = acc + num
        ans = input('do you want to keep going? ')
        count = count + 1
    print('average is {}.'.format(acc/ count))

def average_sentinel():
    acc = 0
    count = 0
    num = 'y'
    while num >= 0:
        num = eval(input('enter number (negative to exit)>> '))
        acc = acc + num
        count = count + 1
    print('average is {}.'.format(acc / count))

if __name__ == '__main__':
    # average()
    # while_average
    # ice_cream()
    # whoops()
    # player_one = 10
    # player_two = 12
    # while not is_game_over(player_one, player_two): # it will loop until one of the players reach 15 points
        # one, two = eval(input('enter score for player one and two: '))
        # player_one = player_one + one
        # player_two = player_two + two
        # print(player_one, player_two)
    # print("GAME OVER! ") # game over at 15 point


