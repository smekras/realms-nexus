"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

import json


def create_json_file(filename, data):
    with open(filename, 'w+') as file:
        json.dump(data, file)


def read_json_file(filename):
    with open(filename, 'r') as source:
        data = json.load(source)
    return data


def set_grid_spacing(grid):
    grid.set_row_spacing(10)
    grid.set_column_spacing(10)
