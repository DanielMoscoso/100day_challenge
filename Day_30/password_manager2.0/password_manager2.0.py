import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# -------------------------- PASSWORD GENERATOR ----------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    number_of_letters = random.randint(8, 10)
    number_of_symbols = random.randint(2, 4)
    number_of_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(number_of_letters):
    #     password_list.append(random.choice(letters))
    password_list += [random.choice(letters) for char in range(number_of_letters)]

    # for char in range(number_of_symbols):
    #     password_list.append(random.choice(symbols))
    password_list += [random.choice(symbols) for char in range(number_of_symbols)]

    # for char in range(number_of_numbers):
    #     password_list.append(random.choice(numbers))
    password_list += [random.choice(numbers) for char in range(number_of_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_text.delete(0, "end")
    password_text.insert("end", string=password)
    pyperclip.copy(password)


# ----------------------------- SAVE PASSWORD -------------------------------- #
def save():
    website_entered = website_text.get()
    mail_user_entered = email_username_text.get()
    password_entered = password_text.get()
    its_ok = False
    try_again = "no"
    new_data = {
        website_entered: {
            "email": mail_user_entered,
            "password": password_entered
        }
    }

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
        try:
            with open("password_manager.json", "r") as data_file:
                # Reading old data:
                data = json.load(data_file)
                # Updating old data with new data:
                data.update(new_data)
        except FileNotFoundError:
            with open("password_manager.json", "w") as data_file:
                # Saving updated data:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("password_manager.json", "w") as data_file:
                # Saving updated data:
                json.dump(data, data_file, indent=4)

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
generate_password = tkinter.Button(text="Generate password", command=generate_password)
add = tkinter.Button(text="add", width=43, command=save)

generate_password.grid(row=3, column=2, sticky='w')
add.grid(row=4, column=1, columnspan=2, sticky='w')


window.mainloop()
