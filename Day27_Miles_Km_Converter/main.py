from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)

def convert():
    km = float(mile_input.get()) * 1.60934
    outcome_label.config(text=f"{km}")

miles_label = Label(text="Miles", font=("Arial", 15))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 15))
km_label.grid(column=2, row=1)

compare_label = Label(text="is equal to", font=("Arial", 15))
compare_label.grid(column=0, row=1)

outcome_label = Label(text=0, font=("Arial", 15))
outcome_label.grid(column=1, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

mile_input = Entry()
mile_input.grid(column=1, row=0)

window.mainloop()