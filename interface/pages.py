"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

from interface.components import *
from interface.graphs import *
from logic.utils import *


class CoreSheet(Frame):
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)

        sheet = read_json_file('data/template.json')
        general = sheet['General']
        attributes = sheet['Attributes']
        secondary = sheet['Secondary']
        skills = sheet['Skills']
        attunement = sheet['Attunement']

        # graph1 = RadarGraph(self, attributes)
        # graph1.place_canvas([1, 0, 1, 1])
        graph2 = RadarGraph(self, attunement)
        graph2.place_canvas([0, 1, 1, 1])

        attuned = Frame(self)

        death = ImageLabel(attuned, "images/death.png")
        death.label.configure(text=attunement['Death'])
        death.frame.grid(row=0, column=0, pady=1)
        matter = ImageLabel(attuned, "images/matter.png")
        matter.label.configure(text=attunement['Matter'])
        matter.frame.grid(row=1, column=0, pady=1)
        ether = ImageLabel(attuned, "images/ether.png")
        ether.label.configure(text=attunement['Ether'])
        ether.frame.grid(row=2, column=0, pady=1)
        energy = ImageLabel(attuned, "images/energy.png")
        energy.label.configure(text=attunement['Energy'])
        energy.frame.grid(row=3, column=0, pady=1)
        life = ImageLabel(attuned, "images/life.png")
        life.label.configure(text=attunement['Life'])
        life.frame.grid(row=4, column=0, pady=1)

        attuned.grid(row=0, column=0)
