import pygame
import sys
from library.colors import *
from library.advanced_figures import *
from library.simple_figures import *
from library.coordinate_system import *

width, height = 1000, 800


def run():

    fps = 100
    dt = int(1000 / fps)

    pygame.init()
    pygame.font.init()

    font = pygame.font.SysFont(None, 16)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Test")
    pygame.display.update()

    radius = 40

    hex_x_input, hex_y_input = 1, 1
    draw_hex(screen, scc(hex_coord_to_xy((hex_x_input, hex_y_input), radius), get_sc_wh(screen)), radius, red, 0)
    pygame.draw.circle(screen, grey, scc(hex_coord_to_xy((hex_x_input, hex_y_input), radius), get_sc_wh(screen)), 10)

    draw_hex(screen, scc(hex_coord_to_xy((0, 0), radius), get_sc_wh(screen)), radius, white, 0)

    # draw_cubic_mesh(screen, 2, radius, font, green, grey)
    # draw_cubic_mesh(screen, 1, radius, font, red, grey)
    draw_circle_mesh(screen, 2, radius, font, green, grey)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # print(clock.tick(dt))
        pygame.display.flip()


# def get_hex1_params(x, y, r):
#     return r/2*s3d2, r*d2


# def draw_hex1(surface, x, y, r, color, width):
#     rd2, rs3d2 = r*d2, r*s3d2
#     coord = (
#         (x, y-r),
#         (x+rs3d2, y-rd2),
#         (x+rs3d2, y+rd2),
#         (x, y+r),
#         (x-rs3d2, y+rd2),
#         (x-rs3d2, y-rd2)
#     )
#     pygame.draw.polygon(surface, color, coord, width)
#     pygame.draw.line(surface, color, (x+rs3d2, y-rd2), (x-rs3d2, y-rd2), width)
#     pygame.draw.line(surface, color, (x-rs3d2, y+rd2), (x+rs3d2, y+rd2), width)
#     pygame.draw.circle(surface, color, (x, y), r, width)


run()
