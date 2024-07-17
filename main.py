from tkinter import *

root = Tk()

root.title("Password Generator")
root.geometry("500x500")

menu = Menu(root)
item = Menu(menu)
item.add_command(label="New")
menu.add_cascade(label="File", menu=item)
root.config(menu=menu)

title_label = Label(root, text="Generate a new password")
title_label.grid()


length = Scale(root, from_=8, to=128, orient=HORIZONTAL, label="Length of password")
numbers = Checkbutton(root, text="Numbers",
                    variable=IntVar(),
                    onvalue=1,
                    offvalue=0)
symbols = Checkbutton(root, text="Symbols",
                      variable=IntVar(),
                      onvalue=1,
                      offvalue=0)


def clicked():
    result = "Password generated"
    title_label.configure(text=result)


length.grid(column=3, row=3)
numbers.grid(column=3, row=4)
symbols.grid(column=3, row=5)
button = Button(root, text="Generate Password", fg="blue", command=clicked)
button.grid(column=2, row=0)

root.mainloop()

