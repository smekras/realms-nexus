"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

from logic import utils

lists = utils.read_json_file('data/lists.json')
qualities = utils.read_json_file('data/qualities.json')
races = utils.read_json_file('data/species.json')

genii = []
for genus in races['Species']:
    genii.append(genus)

avatars = []
for race in races['Species']['Avatar']:
    avatars.append(race)

elementals = []
for race in races['Species']['Elemental']:
    elementals.append(race)

spectrals = []
for race in races['Species']['Spectral']:
    spectrals.append(race)

chimeras = []
for race in races['Species']['Chimera']:
    chimeras.append(race)

cryptids = []
for race in races['Species']['Cryptid']:
    cryptids.append(race)

proteans = []
for race in races['Species']['Protean']:
    proteans.append(race)

eldar = []
for race in races['Species']['Eldar']:
    eldar.append(race)

hauflins = []
for race in races['Species']['Hauflin']:
    hauflins.append(race)

dwarves = []
for race in races['Species']['Dwarf']:
    dwarves.append(race)

humans = []
for race in races['Species']['Human']:
    humans.append(race)

orcs = []
for race in races['Species']['Orc']:
    orcs.append(race)

aspects = []
for aspect in lists['Aspects']:
    aspects.append(aspect)

personae = []
for persona in lists['Personae']:
    personae.append(persona)

bearings = []
for bearing in lists['Bearings']:
    bearings.append(bearing)

primordials = avatars + elementals + spectrals
primals = chimeras + cryptids + proteans
fae = eldar + hauflins
hominids = dwarves + humans + orcs
species = primordials + primals + fae + hominids

taxonomy = {"Genus": genii, "Species": species}
personality = {"Aspect": aspects, "Persona": personae, "Bearing": bearings}
