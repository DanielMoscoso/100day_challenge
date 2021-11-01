import tkinter


# -------------------------- PASSWORD GENERATOR ----------------------------- #

# ----------------------------- SAVE PASSWORD -------------------------------- #
def write_info():
    with open("password_manager.txt", "a") as document:
        document.write(f"Website: {website_text.get()} | E-mail: {email_username_text.get()} | Password: {password_text.get()}\n")


# ------------------------------- UI SETUP ---------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

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

# Entry boxes:
website_text = tkinter.Entry(width=51)
email_username_text = tkinter.Entry(width=51)
password_text = tkinter.Entry(width=32)

website_text.grid(row=1, column=1, columnspan=2, sticky='w')  # sticky="w" > aligned to the left.
email_username_text.grid(row=2, column=1, columnspan=2, sticky='w')
password_text.grid(row=3, column=1, sticky='w')

website_text.focus()
email_username_text.insert("end", "@gmail.com")  # Somehow 'index 0' does not work.

# Buttons:
generate_password = tkinter.Button(text="Generate password")
add = tkinter.Button(text="add", width=43, command=write_info)

generate_password.grid(row=3, column=2, sticky='w')
add.grid(row=4, column=1, columnspan=2, sticky='w')


window.mainloop()
