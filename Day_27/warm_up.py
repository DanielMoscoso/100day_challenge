import tkinter


def button_clicked():
    print("The label got changed.")
    my_label.config(text=input.get())  # "input.get()" gets hold of the value in the input field.


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label:
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# This is how you would update the text in a label:
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Buttons:
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry: (It basically is an input)
input = tkinter.Entry(width=10)  # This creates an input field.
input.grid(column=3, row=2)

window.mainloop()
