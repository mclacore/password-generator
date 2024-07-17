from tkinter import *
import string
import secrets
import pyperclip


def generate_password(length, numbers, symbols):
    if (symbols == 0) and (numbers == 0):
        alphabet = string.ascii_letters
        password = ''.join(secrets.choice(alphabet) for i in range(length))
    elif (symbols == 1) and (numbers == 0):
        alphabet = string.ascii_letters + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
    elif (symbols == 0) and (numbers == 1):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))
    else:
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


def copy_password(password, copy_pass):
    pyperclip.copy(password)
    copy_pass['text'] = "Copied!"


def show_password(password, root, length, show_pass):
    pass_box = Text(root, height=1, width=length.get() + 1)
    pass_box.grid(column=2, row=8, sticky='w')
    pass_box.insert(END, password)
    show_pass['text'] = "Hide Password"
    show_pass['command'] = lambda: hide_password(pass_box, root, length, password, show_pass)


def hide_password(pass_box, root, length, password, show_pass):
    pass_box.grid_remove()
    show_pass['text'] = "Show Password"
    show_pass['command'] = lambda: show_password(password, root, length, show_pass)
