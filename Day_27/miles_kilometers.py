import tkinter


def calculate():
    pass


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# User input:
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

# Labels:
miles = tkinter.Label(text="Miles", font=("Arial", 10, "bold"))
miles.grid(column=2, row=0)

equality = tkinter.Label(text="is equal to", font=("Arial", 10, "bold"))
equality.grid(column=0, row=1)

window.mainloop()
