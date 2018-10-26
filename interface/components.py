"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

import tkinter as tk
from tkinter.ttk import *

from PIL import Image, ImageTk


class ImageLabel(object):
    def __init__(self, parent, image):
        self.frame = Frame(parent)
        pic = Image.open(image)
        pic = pic.resize((32, 32), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(pic)
        self.picture = Label(self.frame, image=self.image, padding=1)
        self.picture.image = self.image
        self.label = Label(self.frame, width=2, padding=1)

        self.picture.grid(row=0, column=0, padx=(0, 5))
        self.label.grid(row=0, column=1)


class LabeledEntry(object):
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.label = Label(self.frame, width=8, padding=1)
        self.entry = Entry(self.frame, width=16)

        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)


class LabeledDropMenu(object):
    def __init__(self, parent):
        frame = Frame(parent)
        self.label = Label(frame, width=8, padding=1)
        self.combo = Combobox(frame, width=14, state="readonly")

        self.label.grid(row=0, column=0)
        self.combo.grid(row=0, column=1)
        frame.pack()


class LabeledAttribute(object):
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.label = Label(self.frame, width=10, padding=1)
        self.base = tk.Spinbox(self.frame, from_=1, to=5, width=3, command=self.update_progress)
        self.bonus = tk.Spinbox(self.frame, from_=0, to=5, width=3, command=self.update_progress)
        self.final = Progressbar(self.frame, maximum=10, length=100)

        self.update_progress()

        self.label.grid(row=0, column=0)
        self.base.grid(row=0, column=1, padx=5)
        self.bonus.grid(row=0, column=2, padx=5)
        self.final.grid(row=0, column=3, padx=5)
        self.frame.pack()

    def update_progress(self):
        base_value = int(self.base.get())
        bonus_value = int(self.bonus.get())
        final_value = base_value + bonus_value

        self.final.configure(value=final_value)


class LabeledNumber(object):
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.label = Label(self.frame, width=10, padding=1)
        self.spin = tk.Spinbox(self.frame, width=3, state="readonly")

        self.label.grid(row=0, column=0)
        self.spin.grid(row=0, column=1, padx=(67, 0))


class LabeledConsumable(object):
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.label = Label(self.frame, width=10, padding=1)
        self.current = tk.Spinbox(self.frame, width=4)
        self.total = tk.Spinbox(self.frame, width=4, state='readonly')

        self.label.grid(row=0, column=0)
        self.current.grid(row=0, column=1, padx=5)
        self.total.grid(row=0, column=2)
