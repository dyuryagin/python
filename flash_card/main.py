from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")




def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(text_title, text="French", fill="black")
    canvas.itemconfig(text_word, text=current_card["French"], fill="black")
    canvas.itemconfig(image_canvas, image=img_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    print(current_card)
    canvas.itemconfig(text_title, text="English", fill="white")
    canvas.itemconfig(text_word, text=current_card["English"], fill="white")
    canvas.itemconfig(image_canvas, image=img_back)

def is_known():
    print(to_learn)
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)

img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")
image_canvas = canvas.create_image(0, 0, image=img_front, anchor="nw")
canvas.grid(row=0, columnspan=2)
text_title = canvas.create_text(400, 150, text="text", fill="black", font=("arial", 40, "italic"))
text_word = canvas.create_text(400, 263, text="word", fill="black", font=("arial", 60, "bold"))


img_wrong = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
btn_wrong.grid(row=1, column=0)

img_right = PhotoImage(file="images/right.png")
btn_right = Button(image=img_right, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
btn_right.grid(row=1, column=1)

flip_timer = window.after(3000, func=flip_card)

next_card()

window.mainloop()