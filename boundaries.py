from typing import *


class Boundaries:
    """ Game boundaries, within which the snake moves """
    def __init__(self):
        # top, bottom, left, and right most value that any boundary can take
        self.limits: Dict[str, int] = {'top': 10, 'bottom': 40, 'left': 50, 'right': 150}
        # edges are used to draw the boundaries on screen
        self.edges: Dict[str, List[Tuple[int, int]]] = {
            'top': [(self.limits['top'], i) for i in range(self.limits['left'], self.limits['right'] + 1)],
            'bottom': [(self.limits['bottom'], i) for i in range(self.limits['left'], self.limits['right'] + 1)],
            'left': [(i, self.limits['left']) for i in range(self.limits['top'], self.limits['bottom'] + 1)],
            'right': [(i, self.limits['right']) for i in range(self.limits['top'], self.limits['bottom'] + 1)]}