from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint

def main():
# main window
    win= GraphWin('Three Door Game II', 1000, 750)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    # Door 1 - draw
    door_1 = Door(Rectangle(Point(1.0, 0.0), Point(3.0, 6.0)), 'Door 1')
    door_1.color_door('Brown')
    door_1.draw(win)
    # Door 2 - draw
    door_2 = Door(Rectangle(Point(4.0, 0.0), Point(6.0, 6.0)), 'Door 2')
    door_2.color_door('Brown')
    door_2.draw(win)
    # Door 3 - draw
    door_3 = Door(Rectangle(Point(7.0, 0.0), Point(9.0, 6.0)), 'Door 3')
    door_3.color_door('Brown')
    door_3.draw(win)

    # draw quit button
    quit_button = Button(Rectangle(Point(7.0, 8.5), Point(9.0, 9.5)), 'Quit')
    quit_button.draw(win)

    # win and lose text box
    wins_text = Text(Point(1.0, 9.25), 'wins')
    wins_text.draw(win)
    wins_box = Rectangle(Point(0.5, 8.5), Point(1.5, 9.0))
    wins_box.draw(win)

    loses_text = Text(Point(2.0, 9.25), 'loses')
    loses_text.draw(win)
    loses_box = Rectangle(Point(1.5, 8.5), Point(2.5, 9.0))
    loses_box.draw(win)

    # accum for loops wins and loses
    wins = 0
    loses = 0

    pt = win.getMouse()
    while not quit_button.is_clicked(pt):
        doors = [door_1, door_2, door_3]
        random_door = randint(0, len(doors) - 1)
        pt = win.getMouse()
        if doors[random_door].is_clicked(pt):














    win.getMouse()
    win.close()

main()