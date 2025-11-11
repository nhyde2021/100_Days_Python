from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -270:
        ball.bounce()

    if ball.distance(r_paddle) < 70 and ball.xcor() > 325:
        ball.hit()

    if ball.distance(l_paddle) < 70 and ball.xcor() < -325:
        ball.hit()

screen.exitonclick()