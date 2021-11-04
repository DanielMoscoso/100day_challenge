import tkinter
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv("./data/Eng-Spa_880_frequency_words.csv")
# ------------------------------- UI SETUP ---------------------------------- #
# Window:
window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Front of flash card:
card_front = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text=data.columns[0], font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text=data["English"][0], font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
# # Back of flash card:
# card_back = tkinter.PhotoImage(file="./images/card_back.png")
# canvas.create_image(400, 263, image=card_back)
# canvas.grid(row=0, column=0)

# Buttons:
image_right = tkinter.PhotoImage(file="./images/right.png")
image_wrong = tkinter.PhotoImage(file="./images/wrong.png")
right_button = tkinter.Button(image=image_right, highlightthickness=0)
wrong_button = tkinter.Button(image=image_wrong, highlightthickness=0)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)
window.mainloop()
