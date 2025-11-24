import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_names = data["state"].to_list()
write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 Guess the State",prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in state_names:
        guessed_states.append(answer_state)
        x = int(data[data["state"] == answer_state]["x"])
        y = int(data[data["state"] == answer_state]["y"])
        write_state.goto(x, y)
        write_state.write(answer_state, align="center", font=("Arial", 10, "normal"))

states_to_learn = [state for state in state_names if state not in guessed_states]

stl = pandas.DataFrame(states_to_learn)
stl.to_csv("states_to_learn.csv")

turtle.mainloop()