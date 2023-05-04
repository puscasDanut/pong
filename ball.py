from turtle import Turtle
import turtle

turtle.addshape("broscoi.gif")

MOVE_DISTANCE_X = 20
MOVE_DISTANCE_Y = 20


class Ball(Turtle):
    global MOVE_DISTANCE_X
    global MOVE_DISTANCE_Y

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color('white')
        self.shape("broscoi.gif")

    def move(self):
        self.setx(self.xcor() + MOVE_DISTANCE_X)
        self.sety(self.ycor() + MOVE_DISTANCE_Y)

    def bounce_y(self):
        global MOVE_DISTANCE_Y
        MOVE_DISTANCE_Y *= -1

    def bounce_x(self):
        global MOVE_DISTANCE_X
        MOVE_DISTANCE_X *= -1

    def should_redirect(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True
        return False

    def reset_position(self):
        self.goto(0, 0)

    def scored(self):
        if self.xcor() > 380:
            return "Left scored"
        elif self.xcor() < -380:
            return "Right scored"
        return

    def is_in_x_range_of_paddle(self):
        if self.xcor() > 330 or self.xcor() < -330:
            return True
        else:
            return False
