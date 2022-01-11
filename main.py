import pygame
import sys
from math import *

width, height = 1400, 1000
s3d2 = sqrt(3) / 2
d2 = 1 / 2


# font = pygame.font.Font('freesansbold.ttf', 32)


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


def get_hex_params(r):
    return 3 * r * d2, r * s3d2


def hex_coord_to_xy(hex_x, hex_y, hex_z, width, height):
    if hex_z % 2 != 0:
        return (hex_x - hex_y) * width, hex_z * height
    else:
        return hex_z * width, (hex_x - hex_y) * height


def draw_hex(surface, x, y, r, color, width):
    rd2, rs3d2 = r * d2, r * s3d2
    coord = (
        (x - r, y),
        (x - rd2, y + rs3d2),
        (x + rd2, y + rs3d2),
        (x + r, y),
        (x + rd2, y - rs3d2),
        (x - rd2, y - rs3d2)
    )
    pygame.draw.polygon(surface, color, coord, width)
    # pygame.draw.line(surface, color, (x-rd2, y+rs3d2), (x-rd2, y-rs3d2), width)
    # pygame.draw.line(surface, color, (x+rd2, y-rs3d2), (x+rd2, y+rs3d2), width)
    # pygame.draw.circle(surface, color, (x, y), r, width)


grey = (128, 128, 128)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test")
pygame.display.set_icon(pygame.image.load("icon.png"))

radius = 5
w, h = get_hex_params(radius)

draw_hex(screen, width / 2, height / 2, radius, white, 0)
# draw_hex(screen, w, h, 100, green, 0)
# draw_hex(screen, 2*w, 0, 100, red, 0)
# draw_hex(screen, 0, 2*h, 100, red, 0)
# draw_hex(screen, 2*w, 2*h, 100, blue, 0)

# hexx, hexy, hexz = 0, -2, 2
# print(hex_coord_to_xy(hexx, hexy, hexz, w, h))
# pygame.draw.circle(screen, grey, hex_coord_to_xy(hexx, hexy, hexz, w, h), 50)

m = 50
for i in range(-m, m):
    for j in range(-m, m):
        for k in range(-m, m):
            if i + j + k == 0:
                if k != m and k != -m and i != m and i != -m and j != m and j != -m:
                    x, y = hex_coord_to_xy(i, j, k, w, h)
                    print(i, j, k)
                    draw_hex(screen, width / 2 + x, height / 2 + y, radius, green, 1)
                else:
                    x, y = hex_coord_to_xy(i, j, k, w, h)
                    print(i, j, k)
                    draw_hex(screen, width / 2 + x, height / 2 + y, radius, grey, 1)

# pygame.draw.line(screen, green, (50, 60), (100, 700), 2)
# pygame.draw.rect(screen, green, (50, 50, 100, 100), 2)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
