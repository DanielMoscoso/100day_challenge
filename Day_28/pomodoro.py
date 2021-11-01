import tkinter
import os
import math
#os.chdir("./Day_28")
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
reps = 0
# ------------------------------- CONSTANTS ---------------------------------- #

# ------------------------------ TIMER RESET --------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # # This is how the wait time should be. The window is not waiting for a process
    # # to end, but instead, a sprecific amount of time to run a command. It does
    # # not matter if it is one on top of the other. It looks like multithreating.
    # count_down(2)
    # window.after(3000, count_down, 3)
    # window.after(7000, count_down, 3)

    cool_down = 0
    for _ in range(8):
        reps += 1
        if reps == 1 or reps == 3 or reps == 5 or reps == 7:
            window.after(cool_down, count_down, work_sec)
            cool_down += (work_sec + 1) * 1000
            print(f"Work for {WORK_MIN}mins")
        elif reps == 8:
            window.after(cool_down, count_down, long_break_sec)
            cool_down += (long_break_sec + 1) * 1000
            print(f"Long break: {LONG_BREAK_MIN}mins")
        elif reps == 2 or reps == 4 or reps == 6:
            window.after(cool_down, count_down, short_break_sec)
            cool_down += (short_break_sec + 1) * 1000
            print(f"Short break: {SHORT_BREAK_MIN}mins")


# -------------------------- COUNTDOWN MECHANISM ----------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"  # dynamic typing: Reasign a 'str' to an existing 'int'.

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ------------------------------- UI SETUP ---------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 145, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label: Timer
timer = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"), highlightthickness=0)
timer.grid(column=1, row=0)

# Button: Start
button1 = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)
# Button: Reset
button2 = tkinter.Button(text="Reset", highlightthickness=0)
button2.grid(column=2, row=2)

# Label: Check mark
check_marks = tkinter.Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"), highlightthickness=0)
check_marks.grid(column=1, row=3)

window.mainloop()
