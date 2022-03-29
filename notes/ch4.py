
    # 2 categories - int, floats, strings
    # 1. class: point, want to group 2 floating points together --> x(float) y(float) - instance variables
    # 1a. constructor: is within the class, can take parameters and create different ranges
    # point()
    # 1b. methods: functions specific to the class, functions that operate one way or the other using the instant variables
    # getx()
    # 2. objects: my_point; is an instance of a class using a constructor

    # my_point = graphics.Point(50, 70)
    # point_a = graphics.Point(70, 90)
    # print(point_a.getX())  # accessor methods
    # x = point_a.getX()
    # print(x + 3)
    # point_a.getY()
    # point_a.move(10, 0)  # point_a.move(move x, move y)
    # print(point_a.move)

    # win = graphics.GraphWin("CSCI 220", 700, 700)  # window where the point it places:
    # default "Graphic Window" title string;
    # 200 width number;
    # 200 height number;
    # (0,0) TOP LEFT ; (700, 700) BOTTOM RIGHT
    # point_a.draw(win)
    # middle = graphics.Point(350, 350)
    # middle.draw(win)
    # input("hit enter to close")
      # program stop at this line

    from graphics import Point, GraphWin, Circle, Text, Polygon, Entry
    # you can get rid of graphics in front of Graphics.Point(350, 350) --> Point(350, 350)

    # my_circle = Circle(middle, 70)  # center (point), radius (float)
    # my_circle.draw
    # input("hit enter to close")


    # create face method1
    # win = GraphWin('Face', 700, 700)
    # label.draw(win)
    # user_input = Entry(Point(5, 5), 50)
    # user_input.setText("Enter your name here ")
    # user_input.draw(win)
    # win.getMouse()
    # name = user_input.getText()
    # label. setText(name)
    # win.getMouse()

    # Face = circle(Point(5, 7), 3)

    # face.draw(win)
    # left_eye.draw(win)
    # right_eye.draw(win)
    # label.draw(win)

    # create a face method 2
    # win = GraphWin('Face', 700, 700)
    # win.setCoords(0, 0, 10, 10)  # everything becomes relative to (0,0) and (10, 10) instead of 0-700 to make it easier

    # face = Circle(Point(5, 8), 3)  # points changed from (350, 100), 100 to this

    # left_eye = Circle(Point(325, 60), 25)
    # left_eye.setFill('yellow')
    # left_eye.setOutline('green')
    # left_eye.setWidth(10)
    # right_eye = left_eye.clone()
    # right_eye.move(50, 0)
    # win.setBackground("light blue")

    # name = Text(Point(350, 600), "Bob")
    # name.draw(win)
    # face.draw(win)
    # left_eye.draw(win)
    # right_eye.draw(win)

    # click_point = win.getMouse()
    # print(click_point.getX(), click_point.getY())

    # Entry method - well always be centered and you can type in the box
    # win = GraphWin('Face', 700, 700)
    # win.setCoords(0, 0, 10, 10)

    # user_input = Entry(Point(5, 5), 30)
    # user_input.setText("enter your name")
    # user_input.draw(win)
    # win.getMouse()
    # name = user_input.getText()
    # print

    # Converting celsius to fahrenheit by text box

    def convert():
        win = GraphWin('Converter', 700, 500)
        win.setCoords(0, 0, 10, 10)
        celsius_text = Text(Point(3, 8), 'Enter Celsius')
        celsius_entry = Entry(Point(7, 8), 30)
        click_text = Text(Point(5, 5), 'Enter to convert')
        result_text = Text(Point(5, 1), '')

        celsius_text.draw(win)
        celsius_entry.draw(win)
        click_text.draw(win)
        win.getMouse()
        celsius = eval(celsius_entry.getText())
        fahrenheit = celsius * 9 / 5 + 32
        result_text.setText(fahrenheit)
        click_text.setText('Click to Close')
        win.getMouse()

convert()



