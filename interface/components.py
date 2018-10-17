from tkinter import *
from tkinter.ttk import *


class LabeledEntry(object):
    def __init__(self, parent):
        frame = Frame(parent)
        self.label = Label(frame, text="placeholder")
        self.entry = Entry(frame)

        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        frame.pack()


class LabeledDropMenu(object):
    def __init__(self, parent):
        frame = Frame(parent)
        self.label = Label(frame, text="placeholder")
        self.combo = Combobox(frame)

        self.label.grid(row=0, column=0)
        self.combo.grid(row=0, column=1)
        frame.pack()
