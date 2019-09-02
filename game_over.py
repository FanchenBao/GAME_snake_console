from typing import *
from boundaries import Boundaries
from functools import reduce


def check(snake: List[Tuple[int, int]], boundaries: Boundaries) -> bool:
    """
    :param snake: repr of snake
    :param boundaries: repr of boundaries
    :return: ture if game is over, otherwise false. The method of check is snake head touches its body or boundaries
    """
    return snake[0] in snake[1:] + reduce(lambda x, y: x + y, boundaries.edges.values())


def restart():
    pass