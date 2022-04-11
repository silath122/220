from door import Door
from button import Button
from graphics import *



def main():
    # main window
    window = GraphWin('Three Door Game I', 400, 700)
    window.setCoords(0.0, 0.0, 10.0, 10.0)

    # draw door
    door_1 = Door(Rectangle(Point(2.0, 0.0), Point(8.0, 7.0)), 'Closed')
    door_1.color_door('Red')
    door_1.draw(window)

    exit_button = Button(Rectangle(Point(2.0, 7.5), Point(8.0, 9.5)), 'Exit')
    exit_button.draw(window)

    pt = window.getMouse()
    while not exit_button.is_clicked(pt):
        if door_1.get_label() == 'Open':
            pt = window.getMouse()
            door_1.is_clicked(pt)
            door_1.close('Red', 'Closed')
            if door_1.get_label() == 'Closed':
                pt = window.getMouse()
                door_1.is_clicked(pt)
                door_1.open('Green', 'Open')
        else:
            if door_1.get_label() == 'Closed':
                pt = window.getMouse()
                door_1.is_clicked(pt)
                door_1.open('Green', 'Open')



    window.getMouse()
    window.close()


main()

# use randint within loop

