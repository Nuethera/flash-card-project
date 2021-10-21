from tkinter import *
import random
import pandas
window = Tk()
BACKGROUND_COLOR = "#B1DDC6"
FRONT = PhotoImage(file="images/card_front.png")
BACK = PhotoImage(file="images/card_back.png")


#--------------CSV logic------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")


data_dict = data.to_dict(orient="records")
word=None

#--------------SAVE LOGIC-----------------#
def right():
    global word, data_dict
    data_dict.remove(word)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    random_card()


#--------------FLASH CAR LOGIC------------#
def show_translation(dict):
    canvas.itemconfig(canvas_image, image=BACK)
    canvas.itemconfig(title_text, text="English",fill='white')
    canvas.itemconfig(word_text, text=f"{dict['English']}",fill='white')
def random_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=FRONT)
    word = random.choice(data_dict)
    canvas.itemconfig(title_text, text="French",fill='black')
    canvas.itemconfig(word_text, text=f"{word['French']}",fill='black')
    flip_timer = window.after(3000, show_translation, word)


#--------------UI SETUP-------------------#

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=FRONT)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

img_right = PhotoImage(file="images/right.png")
right_button = Button(image=img_right, highlightthickness=0, bd=0, command=right)
right_button.grid(column=0, row=1)

img_wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=img_wrong, highlightthickness=0, bd=0, command=random_card)
wrong_button.grid(column=1, row=1)
flip_timer = window.after(10000, show_translation)

random_card()



window.mainloop()
