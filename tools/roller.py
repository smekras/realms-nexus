"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

import random
import tkinter as tk
from tkinter.ttk import *

from interface.components import LabeledEntry


def update_entry(entry, text="", mode=None):
    entry.configure(state=tk.NORMAL)
    entry.delete(0, tk.END)
    entry.insert(0, text)
    if mode == "r":
        entry.configure(state=tk.DISABLED)


class DiceRoller(object):
    def __init__(self, dice=1, sides=10, threshold=7, special=10, use_r=True, use_b=False):
        self.dice = dice
        self.sides = sides
        self.threshold = threshold
        self.special = special
        self.use_rerolls = use_r
        self.use_botches = use_b
        self.successes = 0
        self.botches = 0
        self.results = []

        random.seed()

    def roll_dice(self):
        for i in range(self.dice):
            x = random.randrange(1, self.sides + 1)
            self.results.append(x)
        if self.use_rerolls:
            self.roll_again()

    def roll_again(self):
        re_rolls = len([i for i in self.results if i >= self.special])

        while re_rolls > 0:
            for i in range(re_rolls):
                x = random.randrange(1, self.sides + 1)
                self.results.append(x)
                if x < self.special:
                    re_rolls -= 1

    def get_successes(self):
        s = len([i for i in self.results if i >= self.threshold])
        if self.use_botches:
            self.successes = s - self.get_botches()
        else:
            self.successes = s
        return self.successes

    def get_botches(self):
        self.botches = len([i for i in self.results if i == 1])
        return self.botches


class RollerApp(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.master.title("Nexus - Dice Roller")
        self.master.resizable(False, False)

        self.frame = Frame(self.master)
        self.frame.configure(padding=10)

        self.dice = LabeledEntry(self.frame)
        self.dice.label.configure(text="Number of dice:", width=16)
        self.dice.entry.configure(width=3)

        self.sides = LabeledEntry(self.frame)
        self.sides.label.configure(text="Number of sides:", width=16)
        self.sides.entry.configure(width=3)

        self.threshold = LabeledEntry(self.frame)
        self.threshold.label.configure(text="Success threshold:", width=16)
        self.threshold.entry.configure(width=3)

        self.use_r = tk.IntVar()
        self.use_rerolls = Checkbutton(self.frame, text="Allow rerolls", variable=self.use_r)

        self.special = LabeledEntry(self.frame)
        self.special.label.configure(text="Reroll threshold:", width=16)
        self.special.entry.configure(width=3)

        self.use_b = tk.IntVar()
        self.use_botches = Checkbutton(self.frame, text="Allow botches", variable=self.use_b)

        update_entry(self.dice.entry, "1")
        update_entry(self.sides.entry, "10")
        update_entry(self.threshold.entry, "7")
        update_entry(self.special.entry, "10")

        button = Button(self.frame, text="Roll", command=self.roll_dice)

        self.successes = LabeledEntry(self.frame)
        self.successes.label.configure(text="Successes:", width=16)
        self.successes.entry.configure(state=tk.DISABLED, width=3)

        self.botches = LabeledEntry(self.frame)
        self.botches.label.configure(text="Botches:", width=16)
        self.botches.entry.configure(state=tk.DISABLED, width=3)

        results_label = Label(self.frame, text="Results:")
        self.results = Label(self.frame, wraplength=380, justify=tk.CENTER)

        self.dice.frame.grid(row=0, column=0)
        self.sides.frame.grid(row=1, column=0)
        self.threshold.frame.grid(row=2, column=0)
        self.special.frame.grid(row=3, column=0)
        button.grid(row=4, column=1, sticky="E", pady=10)
        self.successes.frame.grid(row=0, column=1, padx=(10, 0))
        self.botches.frame.grid(row=1, column=1, padx=(10, 0))
        self.use_rerolls.grid(row=2, column=1, sticky="W", padx=(10, 0))
        self.use_botches.grid(row=3, column=1, sticky="W", padx=(10, 0))
        results_label.grid(row=5, column=0, columnspan=2)
        self.results.grid(row=6, column=0, columnspan=2)
        self.frame.pack()

    def roll_dice(self):
        d = int(self.dice.entry.get())
        s = int(self.sides.entry.get())
        t = int(self.threshold.entry.get())
        sp = int(self.special.entry.get())
        u_r = self.use_r.get()
        u_b = self.use_b.get()

        d_roller = DiceRoller(d, s, t, sp, u_r, u_b)
        d_roller.roll_dice()
        d_roller.get_successes()
        d_roller.get_botches()

        self.results.configure(text=d_roller.results)
        update_entry(self.successes.entry, d_roller.successes, "r")
        update_entry(self.botches.entry, d_roller.botches, "r")
