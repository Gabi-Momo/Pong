from turtle import Screen, Turtle
from paddle import Paddle
from pong_ball import Ball
from score_board import Score
import time

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)

# line variables
line = Turtle()
line.setpos(0, -450)
line.color("white")
line.shape("turtle")
line.left(90)

# Center line
while line.ycor() < 420:
    line.forward(25)
    line.pendown()
    line.forward(25)
    line.penup()

paddle_1 = Paddle((550, 0))
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")

paddle_2 = Paddle((-550, 0))
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

ball = Ball()

score_board_l = Score()
score_board_l.setpos(-100, 275)
score_board_l.display_score()

score_board_r = Score()
score_board_r.setpos(100, 275)
score_board_r.display_score()

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.001)
    ball.move()

    # Detect paddle collisions
    if ball.distance(paddle_1) < 45 and ball.xcor() > 545:
        ball.bounce_x()

    if ball.distance(paddle_2) < 45 and ball.xcor() < -545:
        ball.bounce_x()

    # reset ball
    if ball.xcor() > 750:
        score_board_l.increase_score()
        ball.reset()

    if ball.xcor() < -750:
        score_board_r.increase_score()
        ball.reset()

    # Trigger end game
    if score_board_l.score == 10 or score_board_r.score == 10:
        ball.stop()
        score_board_l.game_over()


screen.exitonclick()

