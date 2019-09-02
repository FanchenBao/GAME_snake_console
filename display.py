from typing import *
from boundaries import Boundaries


class Display:
    def __init__(self, boundaries: Boundaries, screen):
        self.bounds = boundaries
        self.screen = screen

    def boundaries(self) -> None:
        """
        :return: None, side-effect: display boundaries on screen
        """
        self.display_char('-', self.bounds.edges['top'] + self.bounds.edges['bottom'])
        self.display_char('|', self.bounds.edges['left'] + self.bounds.edges['right'])

    def food(self, food_: Tuple[int, int]) -> None:
        """
        :param food_: coordinate of food in the form of (row, col)
        :return: None, side-effect: display food on screen
        """
        self.display_char('#', [food_])

    def snake(self, snake_: List[Tuple[int, int]]) -> None:
        """
        :param snake_: coordinates of the snake, starting from head, ending in tail
        :return: None, side-effect: display snake on screen
        """
        self.display_char('@', [snake_[0]])
        self.display_char('*', snake_[1:])

    def score(self, msg: str) -> None:
        """
        :param msg: information about how long the snake has become, serving as a rudimentary scoring system
        :return: None, side-effect: display a message about current snake length on screen
        """
        self.display_msg(
            msg,
            [(self.bounds.limits['top'] - 1, j)
             for j in range(self.bounds.limits['right'] - len(msg), self.bounds.limits['right'])]
        )

    def game_over(self, msg: str) -> None:
        """
        :param msg: game over message
        :return: None, side-effect: display game over message on screen
        """
        self.display_msg(
            msg,
            [(self.bounds.limits['top'] - 1, j)
             for j in range(self.bounds.limits['left'], self.bounds.limits['left'] + len(msg))]
        )

    # utilities
    def display_char(self, char: str, coord_range: List[Tuple[int, int]]) -> None:
        """
        :param screen: the place to display the character on
        :param char: the character to be displayed
        :param coord_range: the range of coordinates where the character should be displayed
        :return: None
        """
        for coord in coord_range:
            self.screen.addstr(*coord, char)

    def display_msg(self, msg: str, coord_range: List[Tuple[int, int]]) -> None:
        """
        :param screen: the place to display the character on
        :param msg: the message to be displayed
        :param coord_range: the range of coordinates to display the message
        :return: None
        """
        for i, coord in enumerate(coord_range):
            self.screen.addstr(*coord, msg[i])
