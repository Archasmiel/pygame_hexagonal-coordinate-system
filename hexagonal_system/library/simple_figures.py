import pygame
from math import sqrt

s3d2 = sqrt(3)/2
d2 = 1/2


# get width and height of hex
def get_hex_params(rad):
    return 3*rad*d2, rad*s3d2


def draw_hex(surface, xy, r, color, line_width):
    rd2, rs3d2 = r * d2, r * s3d2
    coord = (
        (xy[0] - r, xy[1]),
        (xy[0] - rd2, xy[1] + rs3d2),
        (xy[0] + rd2, xy[1] + rs3d2),
        (xy[0] + r, xy[1]),
        (xy[0] + rd2, xy[1] - rs3d2),
        (xy[0] - rd2, xy[1] - rs3d2)
    )
    pygame.draw.polygon(surface, color, coord, line_width)
    # pygame.draw.line(surface, color, (x-rd2, y+rs3d2), (x-rd2, y-rs3d2), width)
    # pygame.draw.line(surface, color, (x+rd2, y-rs3d2), (x+rd2, y+rs3d2), width)
    # pygame.draw.circle(surface, color, (x, y), r, width)
