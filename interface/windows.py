"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

from interface.components import *
from logic import lore


class GeneralPanel(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Labelframe(master, text="General Information", padding=10)

        self.player = LabeledEntry(self.frame)
        self.player.label.configure(text="Player")
        self.player.frame.pack()
        self.name = LabeledEntry(self.frame)
        self.name.label.configure(text="Name")
        self.name.frame.pack()
        self.concept = LabeledEntry(self.frame)
        self.concept.label.configure(text="Concept")
        self.concept.frame.pack()
        self.genus = LabeledDropMenu(self.frame)
        self.genus.label.configure(text="Genus")
        self.genus.combo.configure(values=lore.genii)
        self.genus.combo.bind("<<ComboboxSelected>>", self.update_species)
        self.species = LabeledDropMenu(self.frame)
        self.species.label.configure(text="Species")
        self.species.combo.bind("<<ComboboxSelected>>")
        self.aspect = LabeledDropMenu(self.frame)
        self.aspect.label.configure(text="Aspect")
        self.aspect.combo.configure(values=lore.aspects)
        self.aspect.combo.bind("<<ComboboxSelected>>")
        self.bearing = LabeledDropMenu(self.frame)
        self.bearing.label.configure(text="Bearing")
        self.bearing.combo.configure(values=lore.bearings)
        self.bearing.combo.bind("<<ComboboxSelected>>")
        self.persona = LabeledDropMenu(self.frame)
        self.persona.label.configure(text="Persona")
        self.persona.combo.configure(values=lore.personae)
        self.persona.combo.bind("<<ComboboxSelected>>")

    def update_species(self, event):
        if self.genus.combo.current() == -1:
            self.species.combo.configure(values=lore.species)
        else:
            species = []
            for k, v in lore.races['Species'][self.genus.var.get()].items():
                species.append(k)
            self.species.combo.configure(values=species)


class AttributesPanel(object):
    def __init__(self):
        self.attributes = Labelframe(self, text="Core Attributes", padding=10)

        self.agility = LabeledAttribute(self.attributes)
        self.agility.label.configure(text="Agility")
        self.awareness = LabeledAttribute(self.attributes)
        self.awareness.label.configure(text="Awareness")
        self.charisma = LabeledAttribute(self.attributes)
        self.charisma.label.configure(text="Charisma")
        self.intellect = LabeledAttribute(self.attributes)
        self.intellect.label.configure(text="Intellect")
        self.resilience = LabeledAttribute(self.attributes)
        self.resilience.label.configure(text="Resilience")
        self.strength = LabeledAttribute(self.attributes)
        self.strength.label.configure(text="Strength")
        self.vitality = LabeledAttribute(self.attributes)
        self.vitality.label.configure(text="Vitality")
        self.wits = LabeledAttribute(self.attributes)
        self.wits.label.configure(text="Wits")


class SecondaryPanel(object):
    def __init__(self):
        self.secondary = Labelframe(self, text="Secondary Traits", padding=10)

        self.defence = LabeledNumber(self.secondary)
        self.defence.label.configure(text="Defence")
        self.mass = LabeledNumber(self.secondary)
        self.mass.label.configure(text="Mass")
        self.initiative = LabeledNumber(self.secondary)
        self.initiative.label.configure(text="Initiative")
        self.actions = LabeledNumber(self.secondary)
        self.actions.label.configure(text="Actions")

        self.health = Label(self.secondary, text="Health Points", justify='center')
        self.body = LabeledConsumable(self.secondary)
        self.body.label.configure(text="Body")
        self.will = LabeledConsumable(self.secondary)
        self.will.label.configure(text="Will")
        self.points = LabeledConsumable(self.secondary)
        self.points.label.configure(text="Build Points")
        self.experience = LabeledConsumable(self.secondary)
        self.experience.label.configure(text="Experience")
        self.movement = Label(self.secondary, text="Movement (m/s)", justify='center')
        self.walking = LabeledNumber(self.secondary)
        self.walking.label.configure(text="Walking")
        self.running = LabeledNumber(self.secondary)
        self.running.label.configure(text="Running")
        self.swimming = LabeledNumber(self.secondary)
        self.swimming.label.configure(text="Swimming")
        self.jumping = LabeledNumber(self.secondary)
        self.jumping.label.configure(text="Jumping")

        self.defence.frame.grid(row=0, column=0)
        self.mass.frame.grid(row=1, column=0)
        self.initiative.frame.grid(row=2, column=0)
        self.actions.frame.grid(row=3, column=0)
        self.health.grid(row=5, column=0)
        self.body.frame.grid(row=6, column=0)
        self.will.frame.grid(row=7, column=0)
        self.points.frame.grid(row=0, column=1, padx=(10, 0))
        self.experience.frame.grid(row=1, column=1, padx=(10, 0))
        self.movement.grid(row=3, column=1, padx=(10, 0))
        self.walking.frame.grid(row=4, column=1, padx=(10, 0))
        self.running.frame.grid(row=5, column=1, padx=(10, 0))
        self.jumping.frame.grid(row=6, column=1, padx=(10, 0))
        self.swimming.frame.grid(row=7, column=1, padx=(10, 0))
