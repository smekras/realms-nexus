"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

import tkinter as tk
from tkinter.ttk import *

from PIL import Image, ImageTk


class LabeledWidget(object):
    def __init__(self, master):
        self.frame = Frame(master)
        self.label = Label(self.frame, padding=1)

        self.label.grid(row=0, column=0)


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


class LabeledEntry(LabeledWidget):
    def __init__(self, master):
        super().__init__(master)
        self.label.configure(width=8)
        self.entry = Entry(self.frame, width=16)

        self.entry.grid(row=0, column=1)


class LabeledDropMenu(LabeledWidget):
    def __init__(self, master):
        super().__init__(master)
        self.var = tk.StringVar()
        self.label.configure(width=8)
        self.combo = Combobox(self.frame, textvariable=self.var, width=14, state="readonly")

        self.combo.grid(row=0, column=1)


class LabeledAttribute(LabeledWidget):
    def __init__(self, master):
        super().__init__(master)
        self.label.configure(width=10)
        self.base = tk.Spinbox(self.frame, from_=1, to=5, width=3)
        self.bonus = tk.Spinbox(self.frame, from_=0, to=5, width=3)

        self.base.grid(row=0, column=1, padx=5)
        self.bonus.grid(row=0, column=2, padx=5)


class LabeledNumber(LabeledWidget):
    def __init__(self, master):
        super().__init__(master)
        self.label.configure(width=10)
        self.spin = tk.Spinbox(self.frame, width=3, state="readonly")

        self.spin.grid(row=0, column=1, padx=(67, 0))


class LabeledConsumable(LabeledWidget):
    def __init__(self, master):
        super().__init__(master)
        self.label.configure(width=10)
        self.current = tk.Spinbox(self.frame, width=4)
        self.total = tk.Spinbox(self.frame, width=4, state='readonly')

        self.current.grid(row=0, column=1, padx=5)
        self.total.grid(row=0, column=2)


class SwitchPanel(object):
    def __init__(self, master):
        self.frame = Frame(master)
        pic = Image.open('images/edit.png')
        pic = pic.resize((32, 32), Image.ANTIALIAS)
        self.button = Button(image=pic)
        self.button.image = pic
        self.button.pack()
