from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -270:
        ball.bounce()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 65 and ball.xcor() > 325:
        ball.hit()

    if ball.distance(l_paddle) < 65 and ball.xcor() < -325:
        ball.hit()

    if ball.xcor() > 380:
        scoreboard.l_add_point()
        ball.miss_right()

    if ball.xcor() < -380:
        scoreboard.r_add_point()
        ball.miss_left()


screen.exitonclick()