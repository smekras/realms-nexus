"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

import random


class DiceRoller(object):
    def __init__(self, sides=10, dice=1):
        self.sides = sides
        self.dice = dice
        self.threshold = 7
        self.special = 10
        self.successes = 0
        self.botches = 0
        self.results = []

        random.seed()

    def roll_dice(self):
        for i in range(self.dice):
            x = random.randrange(1, self.sides + 1)
            self.results.append(x)

    def roll_again(self):
        re_rolls = len([i for i in self.results if i >= self.special])

        while re_rolls > 0:
            for i in range(re_rolls):
                x = random.randrange(1, self.sides + 1)
                self.results.append(x)
                re_rolls -= 1
                if x >= self.special:
                    re_rolls += 1

    def get_successes(self):
        self.successes = len([i for i in self.results if i >= self.threshold])
        return self.successes

    def get_botches(self):
        self.botches = len([i for i in self.results if i == 1])
        return self.botches
