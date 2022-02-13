"""
Name: <Siah Thomas>
<hw4>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of square

        # move amount is distance from center of circle to the
        # point where the user clicks
        # click multiple times to move the center of the square
        # move shapes clone
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape2 = shape.clone()
        shape2.move(change_x, change_y)
        shape2.draw(win)
    message = Text(Point(200, 200), "Click again to close")
    message.draw(win)
    win.getMouse()
    win.close()

def rectangle():
    # window
    win = GraphWin("Rectangle", 400, 400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    # get points for rectangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    # draws rectangle
    rect = Rectangle(p1, p2)
    rect.setFill("pink")
    rect.setOutline("red")
    rect.draw(win)

    # display perimeter of rectangle
    per_message = Text(Point(5.0, 3.0), "Perimeter: ")
    per_message.draw(win)
    width = abs(p1.getX() - p2.getX())
    height = abs(p1.getY() - p2.getY())
    perimeter = 2 * (width + height)
    per_num = Text(Point(4.9, 2.5), round(perimeter, 2))
    per_num.draw(win)

    # display area of rectangle
    area_message = Text(Point(5.0, 2.0), "Area: ")
    area_message.draw(win)
    area = width * height
    area_num = Text(Point(4.9, 1.5), round(area, 2))
    area_num.draw(win)

    win.getMouse()
    win.close()

def circle():
    # window
    win = GraphWin("Rectangle", 400, 400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    # get points for circle
    center = win.getMouse()
    center.draw(win)
    circum = win.getMouse()
    circum.draw(win)

    # draw the circle and calculate radius
    radius = float((((circum.getX() - center.getX()) * (circum.getX() - center.getX()))
                    + ((circum.getY() - center.getY()) * (circum.getY() - center.getY()))) ** (1 /2))
    circ = Circle(center, radius)
    circ.draw(win)
    circ.setFill("cyan")
    circ.setOutline("blue")
    radius_message = Text(Point(5.0, 2.0), "Radius: ")
    radius_message.draw(win)
    radius_num = Text(Point(4.8, 1.5), radius)
    radius_num.draw(win)

    # close window
    close_message = Text(Point(5.0, 5.0), "Click again to close")
    close_message.draw(win)
    win.getMouse()
    win.close()

def pi2():
    terms = eval(input("Enter the number of terms to sum: "))



if __name__ == '__main__':
    pass
