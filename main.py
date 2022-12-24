from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snakes = Snake()
food = Food()
scores = ScoreBoard()


screen.listen()
screen.onkey(snakes.up, "w")
screen.onkey(snakes.down, "s")
screen.onkey(snakes.right, "d")
screen.onkey(snakes.left, "a")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)
    snakes.move()

    if snakes.head.distance(food) < 20:
        food.refresh()
        snakes.extend_snake()
        scores.increase()

    if snakes.head.xcor() > 280 or snakes.head.xcor() < -280 or snakes.head.ycor() > 280 or snakes.head.ycor() < -280:
        game_on = False
        scores.game_over()

    for segment in snakes.segments[1:]:
        if snakes.head.distance(segment) < 10:
            game_on = False
            scores.game_over()

screen.exitonclick()


