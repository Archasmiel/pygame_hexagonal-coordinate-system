import pygame
from math import sqrt
from hexagonal_system.library.colors import Color

s3d2 = sqrt(3)/2
d2 = 1/2


def get_hex_params(rad):
    return 3*rad*d2, rad*s3d2


# hexagon drawing function
def draw_hex(surface, xy, r, color: Color, line_width):
    rd2, rs3d2 = r * d2, r * s3d2
    coord = (
        (xy[0] - r, xy[1]),
        (xy[0] - rd2, xy[1] + rs3d2),
        (xy[0] + rd2, xy[1] + rs3d2),
        (xy[0] + r, xy[1]),
        (xy[0] + rd2, xy[1] - rs3d2),
        (xy[0] - rd2, xy[1] - rs3d2)
    )
    pygame.draw.polygon(surface, color.color, coord, line_width)

    # [additional lines and circle around hexagon]
    #
    # pygame.draw.line(surface, color, (x-rd2, y+rs3d2), (x-rd2, y-rs3d2), width)
    # pygame.draw.line(surface, color, (x+rd2, y-rs3d2), (x+rd2, y+rs3d2), width)
    # pygame.draw.circle(surface, color, (x, y), r, width)

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
