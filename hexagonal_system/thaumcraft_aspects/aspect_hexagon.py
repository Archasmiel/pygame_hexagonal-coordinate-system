from hexagonal_system.thaumcraft_aspects.aspects import Aspect
from hexagonal_system.library.coordinates import Coordinates
from hexagonal_system.library.colors import Color

from hexagonal_system.thaumcraft_aspects.aspects import *


class AspectHex:

    def __init__(self, pos: Coordinates, aspect: Aspect):
        self.pos = pos
        self.aspect = aspect

    def get_info(self):
        return [f'{self.pos.x} {self.pos.y}',
                f'{self.aspect.name}']


class AspectGrid:

    def __init__(self, hex_grid: list, cursor_pos: Coordinates):
        self.hex_grid = hex_grid
        self.cursor_pos = cursor_pos
        # self.coord_grid = []


def get_aspect_by_name(name: str) -> Aspect:
    if name == "None":
        return aspect_none
    for i in aspects:
        if i.name == name:
            return i


def get_AspectHex_from_str(line: str):
    lst = line.split(' ')
    return AspectHex(Coordinates(int(lst[0]), int(lst[1])), get_aspect_by_name(lst[2]))


