from tkinter import *
import sys
import os
from menu import create_menu
from password import generate_password, copy_password, show_password, hide_password

def restart_app():
    root.destroy()
    main()

def main():
    global root, length, num_val, sym_val, gen_pass, show_pass
    root = Tk()

    menubar = create_menu(root)
    root.config(menu=menubar)

    root.title("Password Generator")
    root.geometry("300x300")


    title_label = Label(root, text="Generate a new password")
    title_label.grid(column=1, row=1, sticky='w')


    def pass_generated():
        password = generate_password(length.get(), num_val.get(), sym_val.get())

        result = "Password generated"
        title_label.configure(text=result)
        gen_pass.grid_remove()

        copy_pass = Button(root, text="Copy Password", fg="blue", command=lambda: copy_password(password, copy_pass))
        copy_pass.grid(column=1, row=7, sticky='w')

        show_pass = Button(root, text="Show Password", fg="red", command=lambda: show_password(password, root, length, show_pass))
        show_pass.grid(column=1, row=8, sticky='w')

        start_over = Button(root, text="Start Over", fg="black", command=restart_app)
        start_over.grid(column=1, row=9, sticky='w')


    length = Scale(root, from_=8, to=128, orient=HORIZONTAL, label="Length", troughcolor="blue")
    length.grid(column=1, row=3, sticky='w')

    num_val = IntVar()
    numbers = Checkbutton(root, text="Numbers", variable=num_val, onvalue=1, offvalue=0)
    numbers.grid(column=1, row=4, sticky='w')

    sym_val = IntVar()
    symbols = Checkbutton(root, text="Symbols", variable=sym_val, onvalue=1, offvalue=0)
    symbols.grid(column=1, row=5, sticky='w')

    gen_pass = Button(root, text="Generate Password", fg="blue", command=pass_generated)
    gen_pass.grid(column=1, row=6, sticky='w')


    root.mainloop()


if __name__ == "__main__":
    main()
