import pygame.draw

from hexagonal_system.library.simple_figures import draw_hex
from hexagonal_system.library.colors import *
from hexagonal_system.library.coordinates import *


# basic mesh drawing
def draw_mesh(screen, font, coord, mesh, r, hex_color, text_color):
    for i in mesh:
        title = f'{i[0]} {i[1]}'
        fw, fh = font.size(title)
        xy = hex_coord_to_xy(i, r)
        cxy = dot_transfer(coord, xy)
        if i == (0, 0):
            draw_hex(screen, cxy, r, white, 0)
        draw_hex(screen, cxy, r, hex_color, 1)
        screen.blit(font.render(title, True, text_color), dot_transfer(coord, (xy[0] - fw / 2, xy[1] + fh)))
        pygame.draw.circle(screen, hex_color, cxy, int(r / 15))


# dots of square mesh
def get_square_mesh_dots(num):
    build = []
    for i in range(-num, num + 1):
        for j in range(-num, num + 1):
            build.append([i, j])
    return build


# dots of circle mesh
def get_circle_mesh_dots(num):
    i = 0
    build = []
    old = [(0, 0)]
    new = []
    while i <= num:
        for k in old:
            if k not in build:
                build.append(k)
            for j in get_connected_dots(k):
                if j not in build and j not in old:
                    new.append(j)
        old = new.copy()
        new.clear()
        i += 1
    return build


# drawing of hex square mesh
def draw_circle_mesh(screen, font, coord, num, r, hex_color, text_color):
    draw_mesh(screen, font, coord, get_circle_mesh_dots(num), r, hex_color, text_color)


# drawing of hex cubic mesh
def draw_square_mesh(screen, font, coord, num, r, hex_color, text_color):
    draw_mesh(screen, font, coord, get_square_mesh_dots(num), r, hex_color, text_color)


# print square mesh dots to file
def print_square_mesh(num):
    with open(rf'!generated/square/out_{num}.txt', 'w') as f:
        for i in get_square_mesh_dots(num):
            f.write(f'{i[0]} {i[1]}\n')


# print square mesh dots to file
def print_circle_mesh(num):
    with open(rf'!generated/circle/out_{num}.txt', 'w') as f:
        for i in get_circle_mesh_dots(num):
            f.write(f'{i[0]} {i[1]}\n')
