from tkinter import Tk
from password import PasswordGenerator
from menu import MenuBar
from window import Window


class Application:
    def __init__(self):
        self.root = Tk()
        self.password_generator = PasswordGenerator()
        self.menu_bar = MenuBar()
        self.window = Window(
            self.root,
            password_generator=self.password_generator,
            menu_bar=self.menu_bar,
            restart_callback=self.restart
        )


    def run(self):
        self.window.run()


    def restart(self):
        self.root.destroy()
        self.__init__()
        self.run()


if __name__ == '__main__':
    app = Application()
    app.run()
