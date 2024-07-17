from tkinter import *
from menu import create_menu

root = Tk()

menubar = create_menu(root)
root.config(menu=menubar)

root.title("Password Generator")
root.geometry("300x300")


title_label = Label(root, text="Generate a new password")
title_label.grid(column=1, row=1, sticky='w')


def clicked():
    result = "Password generated"
    title_label.configure(text=result)
    copy_pass = Button(root, text="Copy Password", fg="blue", command=clicked)
    copy_pass.grid(column=1, row=7, sticky='w')

    show_pass = Button(root, text="Show Password", fg="blue", command=clicked)
    show_pass.grid(column=1, row=8, sticky='w')


length = Scale(root, from_=8, to=128, orient=HORIZONTAL, label="Length", troughcolor="blue")
length.grid(column=1, row=3, sticky='w')

numbers = Checkbutton(root, text="Numbers", variable=IntVar(), onvalue=1, offvalue=0)
numbers.grid(column=1, row=4, sticky='w')

symbols = Checkbutton(root, text="Symbols", variable=IntVar(), onvalue=1, offvalue=0)
symbols.grid(column=1, row=5, sticky='w')

gen_pass = Button(root, text="Generate Password", fg="blue", command=clicked)
gen_pass.grid(column=1, row=6, sticky='w')




root.mainloop()

