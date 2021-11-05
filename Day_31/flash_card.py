import tkinter
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TIMER = None
SECONDS = 1

RAW_DATA = pd.read_csv("./data/Eng-Spa_860_frequency_words.csv")
DATA_DICT = RAW_DATA.to_dict(orient="records")
RANDOM_WORD = None
KNOWN_WORDS = []
UNKNOWN_WORDS = []


# -------------------------------- Random word --------------------------------
def new_random_word_correct():
    global TIMER
    global RANDOM_WORD
    try:
        window.after_cancel(TIMER)
    except ValueError:
        messagebox.showerror(title="Click Start", message="You need to start the game before anything else.")
    else:
        word_index = DATA_DICT.index(RANDOM_WORD)
        KNOWN_WORDS.append(DATA_DICT.pop(word_index))

        RANDOM_WORD = random.choice(DATA_DICT)
        canvas.itemconfig(canvas_image, image=card_front)
        canvas.itemconfig(language, text=RAW_DATA.columns[0], fill=BACKGROUND_COLOR)
        canvas.itemconfig(word, text=RANDOM_WORD["English"], fill=BACKGROUND_COLOR)
        TIMER = window.after(1000, count_down, SECONDS, RANDOM_WORD)
        print(len(DATA_DICT))  # Debugging


def new_random_word_wrong():
    global TIMER
    global RANDOM_WORD
    try:
        window.after_cancel(TIMER)
    except ValueError:
        messagebox.showerror(title="Click Start", message="You need to start the game before anything else.")
    else:
        UNKNOWN_WORDS.append(RANDOM_WORD)
        unknown_df = pd.DataFrame(UNKNOWN_WORDS)
        unknown_df.to_csv("./data/unknown_words", index=False)

        RANDOM_WORD = random.choice(DATA_DICT)
        canvas.itemconfig(canvas_image, image=card_front)
        canvas.itemconfig(language, text=RAW_DATA.columns[0], fill=BACKGROUND_COLOR)
        canvas.itemconfig(word, text=RANDOM_WORD["English"], fill=BACKGROUND_COLOR)
        TIMER = window.after(1000, count_down, SECONDS, RANDOM_WORD)
        print(len(DATA_DICT))  # Debugging


def known_words():
    window2 = tkinter.Toplevel(window)
    window2.title("Known words")
    window2.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    # Canvas:
    canvas2 = tkinter.Canvas(window2, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_front = tkinter.PhotoImage(file="./images/card_front.png")
    canvas2.create_image(400, 263, image=card_front)

    # Text box:
    text_box = tkinter.Text(window2, height=25, width=80)
    # == Words into 1 string ==
    all_known_words = ""
    for item in KNOWN_WORDS:
        all_known_words += f"{item['English']}: {item['Español']}\n"
    # == Words into 1 string ==
    text_box.insert("end", all_known_words)

    # Label:
    counter = tkinter.Label(window2, text=f"{len(KNOWN_WORDS)}/860", fg="white", bg=BACKGROUND_COLOR, highlightthickness=0, font=("Arial", 20, "bold"))

    counter.grid(row=0, column=0)
    canvas2.grid(row=1, column=0)
    text_box.grid(row=1, column=0)

    window2.mainloop()


def start():
    global TIMER
    global RANDOM_WORD
    RANDOM_WORD = random.choice(DATA_DICT)
    canvas.itemconfig(language, text=RAW_DATA.columns[0], fill=BACKGROUND_COLOR)
    canvas.itemconfig(word, text=RANDOM_WORD["English"], fill=BACKGROUND_COLOR)
    TIMER = window.after(1000, count_down, SECONDS, RANDOM_WORD)
    start.destroy()
    print(len(DATA_DICT))  # Debugging


# -------------------------- COUNTDOWN MECHANISM ----------------------------- #
def count_down(count, random_word):
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1, random_word)
        # print(count)  # Debugging
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

language = canvas.create_text(400, 150, text="Welcome to the game", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Flashcards", font=("Arial", 60, "bold"))
canvas.grid(row=1, column=0, columnspan=3)

# Buttons:
image_right = tkinter.PhotoImage(file="./images/right.png")
image_wrong = tkinter.PhotoImage(file="./images/wrong.png")
right_button = tkinter.Button(image=image_right, highlightthickness=0, command=new_random_word_correct)
wrong_button = tkinter.Button(image=image_wrong, highlightthickness=0, command=new_random_word_wrong)
start = tkinter.Button(width=10, text="Start", highlightthickness=0, command=start)
known = tkinter.Button(width=10, text="Known", highlightthickness=0, command=known_words)

wrong_button.grid(row=2, column=0)
right_button.grid(row=2, column=2)
start.grid(row=2, column=1)
known.grid(row=0, column=2)

window.mainloop()
