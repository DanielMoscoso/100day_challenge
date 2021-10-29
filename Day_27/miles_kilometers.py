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


window.mainloop()
