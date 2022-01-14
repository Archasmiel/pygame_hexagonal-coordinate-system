import sys

from library.advanced_figures import *
from library.simple_figures import *
from library.coordinate_system import *

width, height = 1000, 800


def drawing(screen, font):
    radius = 35
    center = (width/2, height/2-25)

    hex_x_input, hex_y_input = 1, 1
    draw_hex(screen, dot_transfer(hex_coord_to_xy((hex_x_input, hex_y_input), radius), center), radius, red, 0)
    pygame.draw.circle(screen, grey, dot_transfer(hex_coord_to_xy((hex_x_input, hex_y_input), radius), center), 10)

    # draw_square_mesh(screen, font, center, 2, radius, green, grey)
    draw_circle_mesh(screen, font, center, 2, radius, grey, grey)
    # for i in range(6):
    #     print_circle_mesh(i)
    #     print_square_mesh(i)


def run():

    fps = 100
    dt = int(1000 / fps)

    pygame.init()
    pygame.font.init()

    font = pygame.font.SysFont(None, 16)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Hexi")
    pygame.display.set_icon(pygame.image.load("icon.png"))
    pygame.display.update()

    drawing(screen, font)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # print(clock.tick(dt))
        pygame.display.flip()


run()
