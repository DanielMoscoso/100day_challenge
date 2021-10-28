import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label:
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()  # This shows and places the label on the center of the screen.

# This is how you would update the text in a label:
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Buttons:
def button_clicked():
    print("The label got changed.")
    my_label.config(text="You clicked the button")


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()
