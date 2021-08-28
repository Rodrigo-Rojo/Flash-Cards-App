import random
from tkinter import *
import pandas

current_card = {}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

data = data.to_dict(orient="records")


def flip():
    global current_card
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(image, image=card_back_img)
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def right():
    global current_card
    wrong()
    data.remove(current_card)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv", index=False)


def wrong():
    global current_card
    current_card = random.choice(data)

    canvas.itemconfig(image, image=card_front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    window.after(3000, flip)


# Window

window = Tk()
window.title("FlashCard")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)

# Images

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(405, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 300, text="Click to Start", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons

correct_button = Button(image=right_img, highlightthickness=0, command=right, bg=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)


window.mainloop()
