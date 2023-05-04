from turtle import Turtle


class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, -300)
        self.setheading(90)
        self.color('white')
        for _ in range(20):
            self.forward(20)
            self.penup()
            self.forward(10)
            self.pendown()
        self.hideturtle()
