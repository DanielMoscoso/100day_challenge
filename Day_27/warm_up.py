import tkinter


def button_clicked():
    print("The label got changed.")
    my_label.config(text=input.get())  # "input.get()" gets hold of the value in the input field.


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label:
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.place(x=0, y=0)
# This is how you would update the text in a label:
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Buttons:
button = tkinter.Button(text="Click me", command=button_clicked)
button.place(x=200, y=0)

# Entry: (It basically is an input)
input = tkinter.Entry(width=10)  # This creates an input field.
input.place(x=300, y=0)

window.mainloop()
