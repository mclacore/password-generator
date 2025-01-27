"""Generates a password based on the user's input and copies it to the clipboard."""
from tkinter import Text, END
import string
import secrets
import pyperclip


class PasswordGenerator:
    def generate_password(self, length, numbers, symbols):
        """Generates the password based on options"""
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


    def copy_password(self, password, copy_pass):
        """Copies the password to the clipboard."""
        pyperclip.copy(password)
        copy_pass['text'] = "Copied!"


    def show_password(self, password, root, length, show_pass):
        """Shows the password in the text box."""
        pass_box = Text(root, height=1, width=length.get() + 1)
        pass_box.grid(column=2, row=8, sticky='w')
        pass_box.insert(END, password)
        show_pass['text'] = "Hide Password"
        show_pass['command'] = lambda: self.hide_password(pass_box, root, length, password, show_pass)


    def hide_password(self, pass_box, root, length, password, show_pass):
        """Hides the password in the text box"""
        pass_box.grid_remove()
        show_pass['text'] = "Show Password"
        show_pass['command'] = lambda: self.show_password(password, root, length, show_pass)

