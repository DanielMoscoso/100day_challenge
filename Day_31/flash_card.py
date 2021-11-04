import tkinter

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------- UI SETUP ---------------------------------- #
window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Front of flash card:
card_front = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)
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
