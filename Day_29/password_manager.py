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
canvas.grid(row=0, column=1)

# Labels:
website = tkinter.Label(text="Website:")
email_username = tkinter.Label(text="Email/Username:")
password = tkinter.Label(text="Password:")

website.grid(row=1, column=0, sticky="e")  # sticky="e" > aligned to the right.
email_username.grid(row=2, column=0, sticky="e")
password.grid(row=3, column=0, sticky="e")

# Text boxes:
website_text = tkinter.Text(height=1, width=38)
email_username_text = tkinter.Text(height=1, width=38)
password_text = tkinter.Text(height=1, width=24)

website_text.grid(row=1, column=1, columnspan=2, sticky='w')  # sticky="w" > aligned to the left.
email_username_text.grid(row=2, column=1, columnspan=2, sticky='w')
password_text.grid(row=3, column=1, sticky='w')

# Buttons:
generate_password = tkinter.Button(text="Generate password")
add = tkinter.Button(text="add", width=43)

generate_password.grid(row=3, column=2, sticky='w')
add.grid(row=4, column=1, columnspan=2, sticky='w')


window.mainloop()
