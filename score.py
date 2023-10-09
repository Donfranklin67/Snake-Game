from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        self.score = 0
        with open('C:/Users/IGWE/OneDrive/Python/Day-20 Snake game/Snake-Game/data.txt', mode='r') as data:
            self.high_score = int(data.read())
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=-170, y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, 'center', ('ariel', 20, 'bold'))
        self.reset()
        self.max_score()

    def max_score(self):
        self.hideturtle()
        self.penup()
        self.goto(x=170, y=260)
        self.write(f"High Score: {self.high_score}", False, 'center', ('ariel', 20, 'bold'))

    def increase(self):
        self.score += 1
        self.goto(-170, 260)
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('C:/Users/IGWE/OneDrive/Python/Day-20 Snake game/Snake-Game/data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        # self.score = 0
        # self.goto(-170, 260)
        # self.update_score()

    def game_over(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=0)
        self.clear()
        self.write(f"       Game Over !\nYour final score is: {self.score}", False, 'center', ('ariel', 20, 'bold'))
