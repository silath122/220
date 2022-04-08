from door import Door
from button import Button
from graphics import *



def main():
    # main window
    window = GraphWin('Three Door Game I', 400, 700)
    wind = window.setCoords(0.0, 0.0, 10.0, 10.0)

    # draw door
    door_1 = Door(Rectangle(Point(4.0, 0.0), Point(6.0, 7.0)), Text(Point(5.0, 3.5), 'Closed'))
    door_1.color_door('Red')

    exit_button = Button(Rectangle(Point(4.0, 7.5), Point(6.0, 9.5)), Text(Point(5.0, 8.5), 'Exit'))

    pt = wind.getMouse()
    while not exit_button.is_clicked(pt):
        if door_1.is_clicked(pt):
            door_1.open('Green', Text(Point(5.0, 3.5), 'Open'))
            pt = wind.getMouse()
            door_1.is_clicked(pt)

            door_1.close('Red', Text(Point(5.0, 3.5), 'Closed'))
            pt = wind.getMouse()
        wind.getMouse()
    wind.close()



main()





