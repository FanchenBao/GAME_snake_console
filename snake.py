#! /usr/bin/env python3
from typing import *
import curses
import time
from functools import reduce
from random import randint, choice


def display_snake(screen, snake: List[Tuple[int, int]]) -> None:
    """ Draw snake on the screen """
    screen.addstr(*snake[0], '@')
    for segment in snake[1:]:
        screen.addstr(*segment, '*')


def display_boundaries(screen, boundaries: Dict[str, List[Tuple[int, int]]]) -> None:
    """ Draw snake on the screen """
    for coord in boundaries['top'] + boundaries['bot']:
        screen.addstr(*coord, '-')
    for coord in boundaries['lef'] + boundaries['rig']:
        screen.addstr(*coord, '|')


def display_food(screen, food: Tuple[int, int]) -> None:
    """ Display food """
    screen.addstr(*food, '#')


def display_length(screen, top: int, rig: int, length: int) -> None:
    """ Display length of snake on top right corner """
    msg = f"Current Snake Length: {length}"
    for i, coord in enumerate((top - 1, j) for j in range(rig - len(msg), rig)):
        screen.addstr(*coord, msg[i])


def display_game_over(screen, top: int, lef: int) -> None:
    """ Display game over message """
    msg = "Game Over. Press 'ctl + c' to exist."
    for i, coord in enumerate((top - 1, j) for j in range(lef, lef + len(msg))):
        screen.addstr(*coord, msg[i])


def move_snake(snake: List[Tuple[int, int]], direction: Tuple[int, int], eaten: bool) -> List[Tuple[int, int]]:
    """ Change the snake head position based on direction.
        If eaten is true (snake has eaten the food), do not cut tail
    """
    new_head = [(snake[0][0] + direction[0], snake[0][1] + direction[1])]
    new_body = snake[:] if eaten else snake[:-1]
    return new_head + new_body


def create_food(top: int, bot: int, lef: int, rig: int, snake: List[Tuple[int, int]]) -> Tuple[int, int]:
    """ Create a food item randomly in the boundaries but not on snake """
    # Note the scale up in hori
    food = (randint(top + 1, bot - 1), choice(range(lef + 2, rig, 2)))
    return food if food not in snake else create_food(top, bot, lef, rig, snake)


def eat_food(snake: List[Tuple[int, int]], food: Tuple[int, int]) -> bool:
    """ Check whether the snake has eaten the food """
    return snake[0] == food


def game_over(snake: List[Tuple[int, int]], boundaries: Dict[str, List[Tuple[int, int]]]) -> bool:
    """ Check whether game is over: snake head touches its body or boundaries """
    return snake[0] in snake[1:] + reduce(lambda x, y: x + y, boundaries.values())


def main(screen):
    curses.curs_set(0)  # hide cursor
    screen.nodelay(True)  # Don't block I/O calls

    # boundaries, within which snakes can move
    top, bot, lef, rig = 10, 40, 50, 150
    boundaries = {
        'top': [(top, i) for i in range(lef, rig + 1)],
        'bot': [(bot, i) for i in range(lef, rig + 1)],
        'lef': [(i, lef) for i in range(top, bot + 1)],
        'rig': [(i, rig) for i in range(top, bot + 1)]}

    # snake initial position, (row, col) or (y, x). Notice hori scaling up
    snake = [((top + bot) // 2, i) for i in reversed(range(lef, lef + 20, 2))]

    directions = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -2),  # hori need to scale up to match vert
        curses.KEY_RIGHT: (0, 2),
    }
    direction = directions[curses.KEY_RIGHT]  # default direction

    # initial food, not colliding with initial snake
    food = create_food(top, bot, lef, rig, snake)

    while True:  # game loop
        screen.erase()

        # eat food
        eaten = eat_food(snake, food)

        # get direction from user arrowkey input
        direction = directions.get(screen.getch(), direction)
        # move snake accordingly
        snake = move_snake(snake, direction, eaten)

        display_boundaries(screen, boundaries)
        if eaten:
            food = create_food(top, bot, lef, rig, snake)
        display_food(screen, food)
        display_snake(screen, snake)
        display_length(screen, top, rig, len(snake))
        screen.refresh()

        if game_over(snake, boundaries):
            display_game_over(screen, top, lef)
            screen.refresh()
            time.sleep(1000)

        # speed of snake
        time.sleep(0.05)


if __name__ == '__main__':
    curses.wrapper(main)
