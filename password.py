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


def copy_password(password):
    pyperclip.copy(password)
    print('Password copied to clipboard')


def show_password(password):
    print(password)

