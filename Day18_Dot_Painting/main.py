import colorgram
import turtle as t
import random

t.colormode(255)
colors = colorgram.extract('hirst.jpg', 30)

doug = t.Turtle()
doug.shape("turtle")
doug.speed("normal")

def make_dot():
    dot_color = random.choice(colors).rgb
    doug.dot(20, dot_color)
    doug.forward(40)

def create_dot_painting(side_length):
    doug.up()
    dot_count = 0
    for i in range(side_length * 2):
        for _ in range(dot_count):
            make_dot()
        doug.right(90)
        if i % 2 == 0:
            dot_count += 1


create_dot_painting(20)
screen = t.Screen()
screen.exitonclick()