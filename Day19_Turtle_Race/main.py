from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("The Tortuga Derby")
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_on = False

def print_result(string):
    result_turtle = Turtle(shape="turtle")
    result_turtle.up()
    result_turtle.goto(-120,0)
    result_turtle.setheading(270)
    result_turtle.write(string, True, align="center", font=("arial", 12, "normal"))

starting_turtle = Turtle(shape="turtle")
starting_turtle.up()
starting_turtle.goto(230,270)
starting_turtle.down()
starting_turtle.setheading(270)
starting_turtle.forward(500)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-170, -100, -30, 40, 110, 180]
all_turtle = []

for turtle_index in range(0, 6):
    doug = Turtle(shape="turtle")
    doug.color(colors[turtle_index])
    doug.up()
    doug.goto(x=-230,y=y_positions[turtle_index])
    all_turtle.append(doug)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print_result(f"You've won! The {winning_color} turtle is the winner!   ")
            else:
                print_result(f"You've lost. The {winning_color} turtle is the winner.   ")

screen.exitonclick()