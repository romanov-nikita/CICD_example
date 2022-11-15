from tkinter import Tk
from Application import *
from Accountant import *
from callbacks import *


def assign_callbacks(app, acc):
    app.summary_button.config(command=lambda: summary_button(app, acc))
    app.write.config(command=lambda: write_Button(app, acc))


def make_job(root):
    app = Application(root)
    acc = Accountant()
    assign_callbacks(app, acc)

def main():
    root = Tk()
    make_job(root)
    root.mainloop()


if __name__ == "__main__":
    main()
