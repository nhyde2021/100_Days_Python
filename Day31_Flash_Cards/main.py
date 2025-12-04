from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

def next_card():
    global card_timer, current_card
    window.after_cancel(card_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    card_timer = window.after(3000, func=answer)

def answer():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_timer = window.after(3000, answer)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263)
title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_card)
wrong_button.grid(column=0, row=1)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, command=is_known)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()