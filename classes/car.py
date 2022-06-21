import random

class Car():
    def __init__(self):
        self.origin = random.randint(0, 3)
        self.direction = self.genDirection()

    def genDirection(self):
        self.direction = random.randint(0, 3)

        if self.direction == self.origin:
            return self.genDirection()

        return self.direction

    def __str__(self):
        return self.origin
    