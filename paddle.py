from turtle import Turtle

MOVE_DISTANCE = 50


class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(cords)

    def move_up(self):
        diff = 300 - self.ycor()
        if diff == MOVE_DISTANCE:
            return
        if self.ycor() < 300 and self.ycor() > -300:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        diff = 300 + self.ycor()
        if diff == MOVE_DISTANCE:
            return
        if self.ycor() < 300 and self.ycor() > -300:
            self.sety(self.ycor() - MOVE_DISTANCE)
