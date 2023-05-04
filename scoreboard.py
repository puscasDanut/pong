from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Comic Sans', 30, 'bold')


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.penup()
        self.color("white")
        self.score = -1
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, False, align=ALIGNMENT, font=FONT)