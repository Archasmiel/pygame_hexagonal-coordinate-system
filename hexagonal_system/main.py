import sys

import pygame.time

from thaumcraft_aspects.aspect_hexagon import *
from thaumcraft_aspects.aspects_io import draw_aspect_grid

from library.advanced_figures import *
from library.simple_figures import *
from library.coordinates import *

width, height = 1000, 800


def draw_sample(screen, font, clock):
    radius = 45
    center = (width / 2, height / 2 - 25)

    grid = []
    for i in open('!input/in.txt', 'r'):
        grid.append(get_AspectHex_from_str(i.strip()))

    momentum = 0
    power = 10

    for i in get_circle_mesh_dots(2):
        screen.fill(color_black.color)
        draw_aspect_grid(screen, font, (width / 2 + momentum, height / 2 - 25), AspectGrid(grid, Coordinates(i[0], i[1])), radius, color_red,
                         color_green, color_grey)
        pygame.display.update()
        fps_mounter(clock, 75)
        momentum += power


def fps_mounter(clock, fps):
    clock.tick(fps)
    print(clock.get_fps())


def drawing(screen, font):
    radius = 45
    center = (width / 2, height / 2 - 25)

    grid = []
    for i in open('!input/in.txt', 'r'):
        grid.append(get_AspectHex_from_str(i.strip()))

    for i in grid:
        print(i.get_info())

    draw_aspect_grid(screen, font, center, AspectGrid(grid, Coordinates(-2, -1)), radius, color_red, color_green,
                     color_grey)

    # draw_square_mesh(screen, font, center, 2, radius, green, grey)
    # draw_circle_mesh(screen, font, center, 2, radius, grey, grey)
    # for i in range(6):
    #     print_circle_mesh(i)
    #     print_square_mesh(i)


def run():
    fps = 75

    pygame.init()
    pygame.font.init()

    font = pygame.font.SysFont(None, 16)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Hexi")
    pygame.display.set_icon(pygame.image.load("icon.png"))

    drawing(screen, font)
    pygame.display.update()

    drawn = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_sample(screen, font, clock)


run()
