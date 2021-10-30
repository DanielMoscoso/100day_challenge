import tkinter
import os
# ------------------------------- CONSTANTS ---------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
# ------------------------------- CONSTANTS ---------------------------------- #

# ------------------------------ TIMER RESET --------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# -------------------------- COUNTDOWN MECHANISM ----------------------------- #

# ------------------------------- UI SETUP ---------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Label: Timer
label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"), highlightthickness=0)
label.grid(column=2, row=1)

# Button: Start
button1 = tkinter.Button(text="Start")
button1.grid(column=1, row=3)
# Button: Reset
button1 = tkinter.Button(text="Reset")
button1.grid(column=3, row=3)

window.mainloop()
