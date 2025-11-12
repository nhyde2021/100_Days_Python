from turtle import Turtle

GAME_OVER_FONT = ("Courier", 24, "normal")
LEVEL_FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-235, 260)
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=GAME_OVER_FONT)

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=LEVEL_FONT)