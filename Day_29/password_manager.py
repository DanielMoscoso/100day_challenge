import tkinter

# -------------------------- PASSWORD GENERATOR ----------------------------- #

# ----------------------------- SAVE PASSWORD -------------------------------- #

# ------------------------------- UI SETUP ---------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# Lock image:
canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=0)

window.mainloop()
