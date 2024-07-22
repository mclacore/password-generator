"""Adds GUI to password generator"""
from tkinter import Tk, Label, Button, Scale, Checkbutton, IntVar, HORIZONTAL


class Window:
    def __init__(self, root, title="Password Generator", geometry="300x300", password_generator=None, menu_bar=None, restart_callback=None):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        self.password_generator = password_generator
        self.menu_bar = menu_bar
        self.restart_callback = restart_callback

        self.init_menu()

        self.title_label = Label(self.root, text="Generate a new password")
        self.title_label.grid(column=1, row=1, sticky='w')

        self.length = Scale(self.root, from_=8, to=128, orient=HORIZONTAL, label="Length", troughcolor="blue")
        self.length.grid(column=1, row=3, sticky='w')

        self.num_val = IntVar()
        self.numbers = Checkbutton(self.root, text="Numbers", variable=self.num_val, onvalue=1, offvalue=0)
        self.numbers.grid(column=1, row=4, sticky='w')

        self.sym_val = IntVar()
        self.symbols = Checkbutton(self.root, text="Symbols", variable=self.sym_val, onvalue=1, offvalue=0)
        self.symbols.grid(column=1, row=5, sticky='w')

        self.gen_pass = Button(self.root, text="Generate Password", fg="blue", command=self.pass_generated)
        self.gen_pass.grid(column=1, row=6, sticky='w')


    def init_menu(self):
        if self.menu_bar:
            menubar = self.menu_bar.create_menu(self.root)
            self.root.config(menu=menubar)

    
    def restart_app(self):
        if self.restart_callback:
            self.restart_callback()


    def pass_generated(self):
        password = self.password_generator.generate_password(self.length.get(), self.num_val.get(), self.sym_val.get())
        self.title_label.configure(text="Password generated")
        self.gen_pass.grid_remove()

        copy_pass = Button(
            self.root,
            text="Copy Password",
            fg="blue",
            command=lambda: self.password_generator.copy_password(password, copy_pass))
        copy_pass.grid(column=1, row=7, sticky='w')

        show_pass = Button(
            self.root,
            text="Show Password",
            fg="red",command=lambda: self.password_generator.show_password(password, self.root, self.length, show_pass))
        show_pass.grid(column=1, row=8, sticky='w')

        start_over = Button(
            self.root,
            text="Start Over",
            fg="black",
            command=self.restart_app)
        start_over.grid(column=1, row=9, sticky='w')


    def run(self):
        self.root.mainloop()

