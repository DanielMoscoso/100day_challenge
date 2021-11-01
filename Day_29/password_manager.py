import tkinter

# -------------------------- PASSWORD GENERATOR ----------------------------- #

# ----------------------------- SAVE PASSWORD -------------------------------- #

# ------------------------------- UI SETUP ---------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Lock image:
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=0)

# Labels:
website = tkinter.Label(text="Website:")
email_username = tkinter.Label(text="Email/Username:")
password = tkinter.Label(text="Password:")

website.grid(column=0, row=1)
email_username.grid(column=0, row=2)
password.grid(column=0, row=3)

window.mainloop()
