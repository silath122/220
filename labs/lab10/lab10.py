import random
from graphics import *
from door import Door
from button import Button


def main():
    # main window
    Window = GraphWin('Three Door Game I', 400, 700)
    win = Window.setCoords(0.0, 0.0, 10.0, 10.0)

    # select secret door and draw other doors
    door_1 = Door(Rectangle(Point(1.0, 0.0), Point(3.0, 7.0)),
                  Text(Point(2.0, 3.5), 'Closed'))
    door_1.draw(win)
    door_1.color_door('Red')

    door_2 = Door(Rectangle(Point(4.0, 0.0), Point(6.0, 7.0)),
                  Text(Point(5.0, 3.5), 'Closed'))
    door_2.draw(win)
    door_2.color_door('Red')

    door_3 = Door(Rectangle(Point(7.0, 0.0), Point(9.0, 7.0)),
                  Text(Point(8.0, 3.5), 'Closed'))
    door_3.draw(win)
    door_3.color_door('Red')

    rand_door_list = [door_1, door_2, door_3]
    secret = random.choice(rand_door_list)

    if secret:



# my plan
# if win:
    # color clicked to make door green
    # show message -- open
    # keep track of wins?

# if loss:
    # color clicked make red
    # color winning door green
    # display appropriate message
    # keep track of loss?

# if exit:
    # win.close()C


