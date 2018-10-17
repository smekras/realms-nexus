from interface.components import *
from logic import lore


class BaseSheet(object):
    def __init__(self, parent):
        frame = Frame(parent)
        general = Labelframe(frame, text="General Information")

        player = LabeledEntry(general)
        player.label.configure(text="Player:")
        name = LabeledEntry(general)
        name.label.configure(text="Name:")
        concept = LabeledEntry(general)
        concept.label.configure(text="Concept:")
        self.genus = LabeledDropMenu(general)
        self.genus.label.configure(text="Genus:")
        self.genus.combo.configure(values=lore.genii)
        self.genus.combo.bind("<<ComboboxSelected>>", self.update_species)
        self.species = LabeledDropMenu(general)
        self.species.label.configure(text="Species:")

        general.pack()
        frame.pack()

    def update_species(self):
        if self.genus.combo.current() == -1:
            self.species.combo.configure(values=lore.species)
        else:
            self.species.combo.configure(values=lore.races['Species'][self.genus.combo.current()])
