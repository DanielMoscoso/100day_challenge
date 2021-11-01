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
canvas.grid(column=1, row=0)

# Labels:
website = tkinter.Label(text="Website:")
email_username = tkinter.Label(text="Email/Username:")
password = tkinter.Label(text="Password:")

website.grid(column=0, row=1, sticky="e")  # sticky="e" > aligned to the right.
email_username.grid(column=0, row=2, sticky="e")
password.grid(column=0, row=3, sticky="e")

# Text boxes:
website_text = tkinter.Text(height=1, width=38)
email_username_text = tkinter.Text(height=1, width=38)
password_text = tkinter.Text(height=1, width=24)

website_text.grid(column=1, row=1, columnspan=2, sticky='w')  # sticky="w" > aligned to the left.
email_username_text.grid(column=1, row=2, columnspan=2, sticky='w')
password_text.grid(column=1, row=3, sticky='w')

# Buttons:
generate_password = tkinter.Button(text="Generate password")
add = tkinter.Button(text="add", width=43)

generate_password.grid(column=2, row=3, sticky='w')
add.grid(column=1, row=4, columnspan=2, sticky='w')


window.mainloop()
