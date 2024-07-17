from tkinter import *


def create_menu(root):
    menubar = Menu(root)
    create_file_bar(menubar, root)
    create_edit_bar(menubar)
    create_help_bar(menubar)
    return menubar


def create_file_bar(menubar, root):
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file)
    file.add_command(label="New", command=None)
    file.add_command(label="Open", command=None)
    file.add_command(label="Save", command=None)
    file.add_command(label="Exit", command=root.destroy)
    return file


def create_edit_bar(menubar):
    edit = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=edit)
    edit.add_command(label="Cut", command=None)
    edit.add_command(label="Copy", command=None)
    edit.add_command(label="Paste", command=None)
    return edit


def create_help_bar(menubar):
    help = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help)
    help.add_command(label="About", command=None)
    return help
    

