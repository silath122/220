from graphics import *
from random import randint

# is cicked looks for if the button is being passed as clik
# xRange, if its inside the button on the x axis, get the first point
# x value and compare that if x is in between the square
# y value same thing
# color button changes color of the shape
# door is going to look a lot like the button
# get value and use it based on that to open or close door

class Door:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        xRange = (self.shape.getP1().getX() <= point.getX() and point.getX() <= self.shape.getP2().getX())
        yRange = (self.shape.getP1().getY() <= point.getY() and point.getY() <= self.shape.getP2().getY())
        return xRange and yRange

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret






