BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=img)
title_text = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

img_right = PhotoImage(file="images/right.png")
right_button = Button(image=img_right, highlightthickness=0, bd=0)
right_button.grid(column=0, row=1)

img_wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=img_wrong, highlightthickness=0, bd=0)
wrong_button.grid(column=1, row=1)

window.mainloop()
