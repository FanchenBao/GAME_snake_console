from typing import *
from boundaries import Boundaries


def initialize(boundaries: Boundaries, size: int) -> List[Tuple[int, int]]:
    """
    :param boundaries: boundaries within wich the snake moves
    :param size: length of the snake
    :return: list of (row, col) tuples representing the positions of each snake body segment.
    """
    # Also notice the scale up in horizontal direction to match with vertical
    return [((boundaries.limits['top'] + boundaries.limits['bottom']) // 2, i)
            for i in reversed(range(boundaries.limits['left'], boundaries.limits['left'] + 2 * size, 2))]


def eat_food(snake: List[Tuple[int, int]], food: Tuple[int, int]) -> bool:
    """
    :param snake: current repr of snake
    :param food: current position of food
    :return: true if snake has eaten the food, otherwise false
    """
    return snake[0] == food


def move(snake: List[Tuple[int, int]], direction: Tuple[int, int], eaten: bool) -> List[Tuple[int, int]]:
    """
    :param snake: current repr of snake
    :param direction: the direction where the snake has been moving.
    :param eaten: whether food has been eaten by the snake
    :return: a new repr of snake. Change the snake head position based on direction.
            If eaten is true, do not cut tail (because snake will have grown size)
    """
    new_head = [(snake[0][0] + direction[0], snake[0][1] + direction[1])]
    new_body = snake[:] if eaten else snake[:-1]
    return new_head + new_body

