import sys
import math

# Functions
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5


def truncateY(Object):
    if Object.y > 9000:
        Object.y = 9000

    if Object.y < 0:
        Object.y = 0

    Object.y = int(Object.y)


def truncateX(Object):
    if Object.x > 17630:
        Object.x = 17630

    if Object.x < 0:
        Object.x = 0

    Object.x = int(Object.x)
