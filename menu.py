"""Generates GUI menu bar"""
from tkinter import messagebox, Menu


def create_menu(root):
    """Creates the menu bar"""
    menubar = Menu(root)
    create_file_bar(menubar, root)
    create_help_bar(menubar)
    return menubar


def create_file_bar(menubar, root):
    """Creates the file menu bar"""
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file)
    file.add_command(label="Close", command=root.destroy)
    return file


def create_help_bar(menubar):
    """Creates the help menu bar"""
    help_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)
    return help


def about():
    """Displays custom about message"""
    messagebox.showinfo("About", "This is a simple password generator app written by @mclacore.")
