import hexagonal_system.library.simple_figures as sf


class Coordinates:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y

    def get_connected_dots(self):
        if self.x % 2 == 0:
            return [dot_transfer((self.x, self.y), (-1, -1)),
                    dot_transfer((self.x, self.y), (-1, +0)),
                    dot_transfer((self.x, self.y), (+0, +1)),
                    dot_transfer((self.x, self.y), (+1, +0)),
                    dot_transfer((self.x, self.y), (+1, -1)),
                    dot_transfer((self.x, self.y), (+0, -1))]
        else:
            return [dot_transfer((self.x, self.y), (+1, +1)),
                    dot_transfer((self.x, self.y), (-1, +0)),
                    dot_transfer((self.x, self.y), (+0, +1)),
                    dot_transfer((self.x, self.y), (+1, +0)),
                    dot_transfer((self.x, self.y), (-1, +1)),
                    dot_transfer((self.x, self.y), (+0, -1))]


def dot_transfer(coord, transfer):
    return coord[0]+transfer[0], coord[1]+transfer[1]


def get_connected_dots(xy):
    if xy[0] % 2 == 0:
        return [dot_transfer((xy[0], xy[1]), (-1, -1)),
                dot_transfer((xy[0], xy[1]), (-1, +0)),
                dot_transfer((xy[0], xy[1]), (+0, +1)),
                dot_transfer((xy[0], xy[1]), (+1, +0)),
                dot_transfer((xy[0], xy[1]), (+1, -1)),
                dot_transfer((xy[0], xy[1]), (+0, -1))]
    else:
        return [dot_transfer((xy[0], xy[1]), (+1, +1)),
                dot_transfer((xy[0], xy[1]), (-1, +0)),
                dot_transfer((xy[0], xy[1]), (+0, +1)),
                dot_transfer((xy[0], xy[1]), (+1, +0)),
                dot_transfer((xy[0], xy[1]), (-1, +1)),
                dot_transfer((xy[0], xy[1]), (+0, -1))]


def get_sc_wh(screen):
    return screen.get_width(), screen.get_height()


# scc is screen centered coordinates
def scc(coord, centered):
    return centered[0] / 2 + coord[0], centered[1] / 2 + coord[1]


def hex_coord_to_xy(hexes, r):
    wi, he = sf.get_hex_params(r)
    if hexes[0] % 2 == 0:
        return hexes[0]*wi, -hexes[1]*he*2+he
    else:
        return hexes[0]*wi, -hexes[1]*he*2
