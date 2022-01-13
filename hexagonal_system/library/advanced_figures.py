from hexagonal_system.library.simple_figures import *
from hexagonal_system.library.coordinate_system import *


# drawing of hex cubic mesh
def draw_cubic_mesh(screen, num, rad, font, hex_color, text_color):
    """

    :param screen:
    :param num:
    :param rad:
    :param font:
    :param hex_color:
    :param text_color:
    """
    for i in range(-num, num + 1):
        for j in range(-num, num + 1):
            x, y = hex_coord_to_xy((i, j), rad)
            screen.blit(font.render(f'{i} {j}', True, text_color), (screen.get_width()/2+x-10, screen.get_height()/2+y+10))
            draw_hex(screen, scc(hex_coord_to_xy((i, j), rad), get_sc_wh(screen)), rad, hex_color, 1)


def draw_circle_mesh(screen, num, rad, font, hex_color, text_color):
    """

    :param screen:
    :param num:
    :param rad:
    :param font:
    :param hex_color:
    :param text_color:
    """
    f = open('log.txt', 'w')
    i = 0
    build = []
    old = [(0, 0)]
    new = []
    while i < num:
        for k in old:
            if not is_item_in_array(k, build):
                build.append(k)
            connected = get_connected_dots((k[0], k[1]))
            for j in connected:
                if not is_item_in_array(j, build) and not is_item_in_array(j, old):
                    build.append(j)
                    new.append(j)
        old = new.copy()
        new.clear()
        i += 1

    f = open(f'out_{num}.txt', 'w')
    for i in build:
        f.write(f'{i[0]} {i[1]}\n')

    for i in build:
        x, y = hex_coord_to_xy((i[0], i[1]), rad)
        screen.blit(font.render(f'{i[0]} {i[1]}', True, text_color),
                    (screen.get_width() / 2 + x - 10, screen.get_height() / 2 + y + 10))
        draw_hex(screen, scc(hex_coord_to_xy((i[0], i[1]), rad), get_sc_wh(screen)), rad, hex_color, 1)
