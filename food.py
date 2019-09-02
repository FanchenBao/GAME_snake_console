from boundaries import Boundaries
from random import randint, choice
from typing import *


def create(boundaries: Boundaries, snake: List[Tuple[int, int]]) -> Tuple[int, int]:
    """ Create a food item randomly in the boundaries but not on snake, return its coordinate position """
    # Note the scale up in horizontal direction
    food: Tuple[int, int] = (
        randint(boundaries.limits['top'] + 1, boundaries.limits['bottom'] - 1),
        choice(range(boundaries.limits['left'] + 2, boundaries.limits['right'], 2)))
    return food if food not in snake else create()  # food not colliding with snake
