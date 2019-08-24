#! /usr/bin/env python3
# from typing import *
# from time import time
# beg = time()

from typing import *
import curses
import time


def display_snake(screen, snake: List[Tuple[int, int]]) -> None:
    """ Draw snake on the screen """
    screen.addstr(*snake[0], '@')
    for segment in snake[1:]:
        screen.addstr(*segment, '*')


def display_boundaries(screen, boundaries: Dict[str, List[int]]) -> None:
    """ Draw snake on the screen """
    for coord in boundaries['top'] + boundaries['bot']:
        screen.addstr(*coord, '-')
    for coord in boundaries['lef'] + boundaries['rig']:
        screen.addstr(*coord, '|')


def move(screen, snake: List[Tuple[int, int]], direction: Tuple[int, int]) -> List[Tuple[int, int]]:
    """ Change the snake head position based on direction """
    return [tuple(sum(coord) for coord in zip(snake[0], direction))] + snake[:-1]


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

    # snake initial position, (row, col) or (y, x)
    length = 20
    snake = [((top + bot) // 2, i) for i in reversed(range(lef, lef + length))]

    directions = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -1),
        curses.KEY_RIGHT: (0, 1),
    }
    direction = directions[curses.KEY_RIGHT]  # default direction

    while True:  # game loop
        screen.erase()

        # get direction from user arrowkey input
        direction = directions.get(screen.getch(), direction)
        # move snake accordingly
        snake = move(screen, snake, direction)

        display_boundaries(screen, boundaries)
        display_snake(screen, snake)
        screen.refresh()

        # speed of snake
        time.sleep(0.1)


if __name__ == '__main__':
    curses.wrapper(main)
# print("\nTime: {}".format(time() - beg))
