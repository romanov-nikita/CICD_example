from tkinter import W, E
from tkinter.ttk import Frame, Button, Entry, Style, Combobox, Label


states = ('Доход', 'Расход')


class Application(Frame):

    def __init__(self, parent):
        super().__init__()
        self.summary_label = None
        self.summary_button = None
        self.write = None
        self.combo = None
        self.entry = None
        self.parent = parent
        self.initUI()
        self.centerWindow()

    def initUI(self):
        self.master.title("Личный счетчик")

        Style().configure("TButton", font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)

        self.entry = Entry(self)
        self.entry.grid(row=0, column=1)
        self.combo = Combobox(self)
        self.combo.grid(row=0, column=0)
        self.combo['values'] = states
        self.combo['state'] = 'readonly'
        self.combo.set(states[0])
        self.write = Button(self, text='Записать')
        self.write.grid(row=1, column=1, sticky=W+E)
        label = Label(self)
        label.grid(row=1, column=0, sticky=W+E)
        self.summary_label = Label(self, text="0 Р.", anchor='center')
        self.summary_label.grid(row=2, column=0, sticky=W+E)
        self.summary_button = Button(self, text='Итог')
        self.summary_button.grid(row=2, column=1, sticky=W+E)

        self.pack()

    def centerWindow(self):
        w = 280
        h = 110

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))