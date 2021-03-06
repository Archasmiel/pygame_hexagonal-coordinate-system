from hexagonal_system.thaumcraft_aspects.aspect_hexagon import *
from hexagonal_system.thaumcraft_aspects.aspects import *
from hexagonal_system.library.colors import *
from hexagonal_system.library.coordinates import *
from hexagonal_system.library.simple_figures import *


def get_connected_aspects(item: Aspect, params: tuple) -> list:
    res = []
    if params[1]:
        for i in aspects:
            if (i.get_aspects()[0] is item) or (i.get_aspects()[1] is item):
                res.append(i)
    if params[0] and item not in basic:
        if item.first is not None:
            res.append(item.first)
        if item.second is not None:
            res.append(item.second)
    return res


def deduplicate(aspects_list: list):
    res = []
    for i in aspects_list:
        if i not in res:
            res.append(i)
    return res


def aspect_to_basic(item: Aspect, strings: bool):
    res = [item]
    temp = []
    workable = True

    while workable:
        counter = len(res)

        for i in res:
            if i.level > 0:
                temp.append(i.first)
                temp.append(i.second)
            else:
                temp.append(i)
                counter -= 1

        if counter == 0:
            workable = False

        res = temp.copy()
        temp.clear()
    if strings:
        temp = [0]*6
        for i in sorted([i.name for i in res]):
            for j, val in enumerate(basic):
                if i == val.name:
                    temp[j] += 1
        res = [[basic[i].name, temp[i]] for i in range(len(basic))]
        return res
    else:
        return res


def draw_aspect_grid(screen, font, coord: tuple, grid: AspectGrid, r: int,
                     cursor_color: Color, hex_color: Color, text_color: Color):
    cursor_xy = dot_transfer(hex_coord_to_xy((grid.cursor_pos.x, grid.cursor_pos.y), r), coord)
    draw_hex(screen, cursor_xy, r, cursor_color, 0)
    pygame.draw.circle(screen, text_color.color, cursor_xy, 10)

    for i in grid.hex_grid:
        titles = i.get_info()
        fw1, fh1 = font.size(titles[0])
        fw2, fh2 = font.size(titles[1])
        xy = hex_coord_to_xy(i.pos.get_coord(), r)
        cxy = dot_transfer(coord, xy)
        if i == (0, 0):
            draw_hex(screen, cxy, r, white, 0)
        draw_hex(screen, cxy, r, hex_color, 1)
        screen.blit(font.render(titles[0], True, text_color.color),
                    dot_transfer(coord, (xy[0] - fw1 / 2, xy[1] + 0.5 * fh1)))
        screen.blit(font.render(titles[1], True, text_color.color),
                    dot_transfer(coord, (xy[0] - fw2 / 2, xy[1] + 1.5 * fh2)))
        pygame.draw.circle(screen, hex_color.color, cxy, int(r / 15))


def get_combinations_of_grid(grid: AspectGrid):
    # TODO
    pass
    # for i in grid.hex_grid:
    #     if grid.cursor_pos is i.:
