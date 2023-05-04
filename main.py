from turtle import Screen
from paddle import Paddle
from time import sleep
from ball import Ball
from scoreboard import Score
from field import Field

if __name__ == '__main__':
    screen = Screen()
    screen.tracer(0)
    paddle_r = Paddle((350, 0))
    paddle_l = Paddle((-350, 0))
    ball = Ball()
    score_r = Score((75, 225))
    score_l = Score((-75, 225))
    field = Field()

    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title("Cristi's Pong")

    screen.listen()
    screen.onkeypress(key="Down", fun=paddle_l.move_down)
    screen.onkeypress(key="Up", fun=paddle_l.move_up)
    screen.onkeypress(key="w", fun=paddle_r.move_up)
    screen.onkeypress(key="s", fun=paddle_r.move_down)

    game_over = False

    while not game_over:
        screen.update()
        sleep(0.1)
        ball.move()
        if ball.should_redirect():
            ball.bounce_y()
        if ball.scored() == "Right scored":
            score_r.increase_score()
            ball.reset_position()
        elif ball.scored() == "Left scored":
            score_l.increase_score()
            ball.reset_position()
        if ball.is_in_x_range_of_paddle() and (ball.distance(paddle_l) < 50 or ball.distance(paddle_r) < 50):
            ball.bounce_x()
    screen.exitonclick()
