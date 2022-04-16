from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint

def main():
# main window
    win= GraphWin('Three Door Game II', 1000, 750)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    win.setBackground('Lightblue1')

    # Door 1 - draw
    door_1 = Door(Rectangle(Point(1.0, 0.0), Point(3.0, 6.0)), 'Door 1')
    door_1.color_door('Sienna')
    door_1.draw(win)
    # Door 2 - draw
    door_2 = Door(Rectangle(Point(4.0, 0.0), Point(6.0, 6.0)), 'Door 2')
    door_2.color_door('Sienna')
    door_2.draw(win)
    # Door 3 - draw
    door_3 = Door(Rectangle(Point(7.0, 0.0), Point(9.0, 6.0)), 'Door 3')
    door_3.color_door('Sienna')
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

    # play again message and changing message
    play_again_text = Text(Point(5.0, 7.00), 'Click to to guess which is the secret door!')
    play_again_text.draw(win)
    diff_message = Text(Point(5.0, 7.50), 'I have a secret door.')
    diff_message.draw(win)

    # accum for loops wins and loses
    wins = 0
    loses = 0
    wins_text = Text(Point(1.0, 8.75), wins)
    wins_text.draw(win)
    loses_text = Text(Point(2.0, 8.75), loses)
    loses_text.draw(win)

    pt = win.getMouse()
    while not quit_button.is_clicked(pt):
        doors = [door_1, door_2, door_3]
        random_door = randint(0, len(doors) - 1)
        pt = win.getMouse()
        if doors[random_door].is_clicked(pt):
            doors[random_door].color_door("Green")
            diff_message.setText('you win!')
            play_again_text.setText('Click to play again!')
            wins += 1
            wins_text.setText(wins)
            win.getMouse()
            for each_door in doors:
                each_door.color_door('Sienna')
            pt = win.getMouse()

        else:
            if doors[random_door].is_clicked(pt) == False:
                for each_door in doors:
                    each_door.color_door('Red')
                doors[random_door].color_door("Green")
                diff_message.setText('incorrect, try again!')
                play_again_text.setText('Click to play again!')
                loses += 1
                loses_text.setText(loses)
                win.getMouse()
                for each_door in doors:
                    each_door.color_door('Sienna')
                pt = win.getMouse()
    pt = win.getMouse()
    if quit_button.is_clicked(pt):
        win.close()

main()