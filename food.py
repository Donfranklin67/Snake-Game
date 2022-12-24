from turtle import Turtle
import random

SHAPE = ['square', 'triangle', 'circle', 'classic']


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(0.7)
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 270)
        self.shape(random.choice(SHAPE))
        self.goto(x=rand_x, y=rand_y)
