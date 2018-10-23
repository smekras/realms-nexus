"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""


class Entity(object):
    def __init__(self):
        self.name = ""
        self.notes = ""


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.email = ""
        self.characters = []


class Person(Entity):
    def __init__(self):
        super().__init__()
        self.attributes = []
        self.skills = []
        self.qualities = []
        self.powers = []


class Character(Person):
    def __init__(self):
        super().__init__()
        self.player = ""
        self.concept = ""
        self.genus = []
        self.species = []
        self.aspect = []
        self.bearing = []
        self.persona = []
        self.quirk = ""
        self.forms = []
        self.augmentations = []
        self.identities = []
        self.lifestyles = []
        self.assets = []
        self.weapons = []
        self.outfits = []
        self.commlinks = []
        self.systems = []
        self.companions = []
        self.vehicles = []
        self.eidolons = []


class Companion(Person):
    def __init__(self):
        super().__init__()
        self.type = ""
        self.loyalty = ""


class Augmentation(Entity):
    def __init__(self):
        super().__init__()
        self.type = ""
        self.rating = 0
        self.bleed = 0


class Identity(Entity):
    def __init__(self):
        super().__init__()
        self.rating = 0
        self.lifestyle = 0
        self.licenses = []


class Asset(Entity):
    def __init__(self):
        super().__init__()
        self.rating = 0
        self.quantity = 0
        self.cost = 0


class Lifestyle(Asset):
    def __init__(self):
        super().__init__()
        self.id = 0


class Weapon(Asset):
    def __init__(self):
        super().__init__()
        self.damage = 0
        self.piercing = 0


class MeleeWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.reach = 0


class RangedWeapon(Weapon):
    def __init__(self):
        super().__init__()
        self.mode = ""
        self.reload = ""
        self.ranges = [0, 0, 0, 0]


class Outfit(Asset):
    def __init__(self):
        super().__init__()
        self.armour = [0, 0, 0]


class Vehicle(Entity):
    def __init__(self):
        super().__init__()
        self.attributes = []
        self.software = []
        self.accessories = []
        self.weapons = []


class Eidolon(Entity):
    def __init__(self):
        super().__init__()
        self.type = ""
        self.attributes = []
        self.software = []
