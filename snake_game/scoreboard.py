from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.showscore()

    def increase(self):
        self.score += 1
        self.showscore()

    def showscore(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 20, "normal"))