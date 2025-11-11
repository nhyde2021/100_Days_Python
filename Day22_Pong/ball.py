from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.16

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def miss_right(self):
        self.ball_speed = 0.16
        self.goto(0, 0)
        self.hit()

    def miss_left(self):
        self.ball_speed = 0.16
        self.goto(0, 0)
        self.hit()