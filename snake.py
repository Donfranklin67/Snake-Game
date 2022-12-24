import turtle as t
import random


STARTING_POSITIONS = [(0, 0), (40, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        t.colormode(255)
        tim = t.Turtle("circle")
        tim.color(self.colour())
        tim.shapesize(2)
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend_snake(self):
        self.add_snake(self.segments[-1].position())

    def colour(self):
        r = random.randint(1, 200)
        g = random.randint(1, 200)
        b = random.randint(1, 200)
        new_colour = (r, g, b)
        return new_colour

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x=new_x, y=new_y)
        self.head.forward(20)
        
    def reset(self):
        for parts in self.segments:
            parts.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
