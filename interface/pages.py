"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

from interface.components import *
from interface.graphs import *


class CoreSheet(Frame):
    def __init__(self, parent, source, **kw):
        super().__init__(parent, **kw)
        sheet = source
        # general = sheet['General']
        attributes = source.attributes
        # secondary = sheet['Secondary']
        skills = source.skills
        attunement = source.powers

        general = Frame(self)

        pic = Image.open(sheet.image)
        # pic = pic.resize((32, 32), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(pic)
        self.picture = Label(general, image=self.image, padding=1)
        self.picture.image = self.image
        self.picture.grid(row=0, column=0)

        name = Label(general, text=sheet.name).grid(row=1, column=0)
        marquee = str(sheet.species[0]) + " " + str(sheet.genus[0]) + " " + str(sheet.aspect[0]) + " (" + str(
            sheet.concept) + "). "
        personality = str(sheet.bearing[0]) + " - " + str(sheet.persona[0]) + ": " + sheet.quirk
        marquee_label = Label(general, text=marquee).grid(row=2, column=0)
        personality_label = Label(general, text=personality).grid(row=3, column=0)

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

        general.grid(row=0, column=0, padx=(0, 10))
        attuned.grid(row=0, column=1)

        # graph1 = RadarGraph(self, attributes)
        # graph1.place_canvas([1, 0, 1, 1])
        graph2 = RadarGraph(self, attunement)
        graph2.place_canvas([0, 2, 1, 1])
