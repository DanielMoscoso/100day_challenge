import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TIMER = None
SECONDS = 3

RAW_DATA = pd.read_csv("./data/Eng-Spa_880_frequency_words.csv")
DATA_DICT = RAW_DATA.to_dict(orient="records")


# -------------------------------- Random word --------------------------------
def new_random_word_correct():
    global TIMER
    window.after_cancel(TIMER)
    random_word = random.choice(DATA_DICT)
    canvas.itemconfig(language, text=RAW_DATA.columns[0])
    canvas.itemconfig(word, text=random_word["English"])
    TIMER = window.after(1000, count_down, SECONDS, random_word)


def new_random_word_wrong():
    global TIMER
    window.after_cancel(TIMER)
    random_word = random.choice(DATA_DICT)
    canvas.itemconfig(language, text=RAW_DATA.columns[0])
    canvas.itemconfig(word, text=random_word["English"])
    TIMER = window.after(1000, count_down, SECONDS, random_word)


def start():
    global TIMER
    random_word = random.choice(DATA_DICT)
    canvas.itemconfig(language, text=RAW_DATA.columns[0])
    canvas.itemconfig(word, text=random_word["English"])
    TIMER = window.after(1000, count_down, SECONDS, random_word)
    start.destroy()


# -------------------------- COUNTDOWN MECHANISM ----------------------------- #
def count_down(count, random_word):
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1, random_word)
        print(count)
    else:
        canvas.itemconfig(canvas_image, image=card_back)
        canvas.itemconfig(language, fill="white", text=RAW_DATA.columns[1])
        canvas.itemconfig(word, fill="white", text=random_word["Español"])
        canvas.itemconfig(word, fill="white")


# ------------------------------- UI SETUP ---------------------------------- #
# Window:
window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Front and back of flash card:
card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front)

language = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

# Buttons:
image_right = tkinter.PhotoImage(file="./images/right.png")
image_wrong = tkinter.PhotoImage(file="./images/wrong.png")
right_button = tkinter.Button(image=image_right, highlightthickness=0, command=new_random_word_correct)
wrong_button = tkinter.Button(image=image_wrong, highlightthickness=0, command=new_random_word_wrong)
start = tkinter.Button(width=10, text="Start", highlightthickness=0, command=start)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=2)
start.grid(row=1, column=1)

window.mainloop()
