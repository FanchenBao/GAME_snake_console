#! /usr/bin/env python3
from typing import *
import curses
import time
from functools import reduce


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


def display_game_over(screen, top: int, lef: int) -> None:
    """ Display game over message """
    msg = "Game Over. Press 'ctl + c' to exist."
    for i, coord in enumerate((top - 1, j) for j in range(lef, lef + len(msg))):
        screen.addstr(*coord, msg[i])


def move_snake(screen, snake: List[Tuple[int, int]], direction: Tuple[int, int]) -> List[Tuple[int, int]]:
    """ Change the snake head position based on direction """
    return [(snake[0][0] + direction[0], snake[0][1] + direction[1])] + snake[:-1]


def game_over(snake: List[Tuple[int, int]], boundaries: Dict[str, List[Tuple[int, int]]]) -> bool:
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
    length = 20
    snake = [((top + bot) // 2, i) for i in reversed(range(lef, lef + length, 2))]

    directions = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -2),  # hori need to scale up to match vert
        curses.KEY_RIGHT: (0, 2),
    }
    direction = directions[curses.KEY_RIGHT]  # default direction

    # initial food

    while True:  # game loop
        screen.erase()

        # get direction from user arrowkey input
        direction = directions.get(screen.getch(), direction)
        # move snake accordingly
        snake = move_snake(screen, snake, direction)

        display_boundaries(screen, boundaries)
        display_snake(screen, snake)
        screen.refresh()

        if game_over(snake, boundaries):
            display_game_over(screen, top, lef)
            screen.refresh()
            time.sleep(1000)

        # speed of snake
        time.sleep(0.1)


if __name__ == '__main__':
    curses.wrapper(main)
