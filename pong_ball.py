from turtle import Turtle

heading = 315


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.setpos(0, 0)
        self.color("white")
        self.shape("square")
        self.shapesize(1)
        self.penup()
        self.setheading(heading)
        self.speed = 5

    def move(self):
        self.forward(self.speed)
        if self.ycor() < -375:
            self.bounce()
        if self.ycor() > 375:
            self.bounce()

    def bounce(self):
        new_heading = self.setheading(360 - self.heading())
        heading = new_heading

    def bounce_x(self):
        self.setheading(180 - self.heading())
        self.speed += .5

    def reset(self):
        self.setpos(0, 0)
        self.speed = 5

    def stop(self):
        self.speed = 0
