from random import randint


class Die:
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        new_value = randint(1, self.sides)
        self.value = new_value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

# getter and setters, set the value or get the value