from turtle import Turtle
FONT = ("Impact", 60, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(25)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")

    def display_score(self):
        self.write(f"{self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
