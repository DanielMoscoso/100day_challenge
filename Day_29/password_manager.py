import tkinter
from tkinter import messagebox


# -------------------------- PASSWORD GENERATOR ----------------------------- #

# ----------------------------- SAVE PASSWORD -------------------------------- #
def save():
    website_entered = website_text.get()
    mail_user_entered = email_username_text.get()
    password_entered = password_text.get()
    its_ok = False
    try_again = "no"

    # If any of the fields is empty:
    if len(website_entered) == 0 or len(mail_user_entered) < 13 or len(password_entered) == 0:
        try_again = messagebox.showwarning(title="Oops!", message="Don't leave any field empty!")
    else:
        its_ok = messagebox.askokcancel(title=website_entered, message=f"These are the details entered:\n"
                                                                       f"\nEmail: {mail_user_entered}"
                                                                       f"\nPassword: {password_entered}\n"
                                                                       f"\nIs it ok to save?")

    # If no field is left empty, and the user is satisfied with the information entered:
    if try_again != "ok" and its_ok:
        with open("password_manager.txt", "a") as document:
            document.write(f"Website: {website_entered} | E-mail: {mail_user_entered} | Password: {password_entered}\n")
            website_text.delete(0, "end")
            email_username_text.delete(0, "end")
            password_text.delete(0, "end")

            website_text.focus()
            email_username_text.insert("end", string="@gmail.com")


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
email_username_text.insert("end", string="@gmail.com")  # Somehow 'index 0' does not work.

# Buttons:
generate_password = tkinter.Button(text="Generate password")
add = tkinter.Button(text="add", width=43, command=save)

generate_password.grid(row=3, column=2, sticky='w')
add.grid(row=4, column=1, columnspan=2, sticky='w')


window.mainloop()
