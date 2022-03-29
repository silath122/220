from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())

def triangle():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    tri = Polygon(p1, p2, p3)
    tri.setFill("peachpuff")
    tri.setOutline("cyan")
    tri.draw(win)
    message.setText("Click anywhere to quit.")
    win.getMouse()

def convert_guy():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(1, 3), "   Celsius Temperature: ").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature: ").draw(win)
    input = Entry(Point(2, 3), 5)
    input.draw(win)
    input.setText("0.0")
    output = Text(Point(2, 1), " ")
    output.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    # wait for a mouse click
    win.getMouse()

    # convert input
    celsius = eval(input.getText())
    fahrenheit = 9.0/5.0 * celsius + 32

    # display output and change button
    output.setText(fahrenheit)
    button.setText("Quit")

    # wait for click and then click
    win.getMouse()
    win.close()

convert_guy()

