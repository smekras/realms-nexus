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
        self.email = []
        self.characters = []


class Person(Entity):
    def __init__(self, source):
        super().__init__()
        self.image = source['General']['Images'][0]
        self.name = source['General']['Name']
        self.attributes = source['Attributes']
        self.skills = source['Skills']
        self.qualities = source['Qualities']
        self.powers = source['Attunement']
        self.notes = ""


class Character(Person):
    def __init__(self, source):
        super().__init__(source)
        self.player = source['General']['Player']
        self.concept = source['General']['Concept']
        self.genus = source['General']['Genus']
        self.species = source['General']['Species']
        self.aspect = source['General']['Aspect']
        self.bearing = source['General']['Bearing']
        self.persona = source['General']['Persona']
        self.quirk = source['Personality']['Quirk']
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
