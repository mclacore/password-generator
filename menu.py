from tkinter import *
from tkinter import messagebox


def create_menu(root):
    menubar = Menu(root)
    create_file_bar(menubar, root)
    create_help_bar(menubar)
    return menubar


def create_file_bar(menubar, root):
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file)
    file.add_command(label="Close", command=root.destroy)
    return file


def create_help_bar(menubar):
    help = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help)
    help.add_command(label="About", command=about)
    return help


def about():
    messagebox.showinfo("About", "This is a simple password generator app written by @mclacore.")

