import curses
import time

# custom import
from boundaries import Boundaries
import snake
import food
from display import Display
import game_over


def main(screen):
    def game() -> None:
        curses.curs_set(0)  # hide cursor
        screen.nodelay(True)  # Don't block I/O calls

        # boundaries, within which snakes can move
        boundaries = Boundaries()

        # initialize snake
        snake_ = snake.initialize(boundaries, 10)

        directions = {
            curses.KEY_UP: (-1, 0),
            curses.KEY_DOWN: (1, 0),
            curses.KEY_LEFT: (0, -2),  # hori need to scale up to match vert
            curses.KEY_RIGHT: (0, 2),
        }
        direction = directions[curses.KEY_RIGHT]  # default direction

        # initial food
        food_ = food.create(boundaries, snake_)

        # initialize display
        display = Display(boundaries, screen)

        while True:  # game loop
            screen.erase()

            # check whether snake has eaten the food
            eaten = snake.eat_food(snake_, food_)
            if eaten:
                food_ = food.create(boundaries, snake_)

            # get direction from user arrow key input
            direction = directions.get(screen.getch(), direction)
            # move snake accordingly
            snake_ = snake.move(snake_, direction, eaten)

            # display game elements
            display.boundaries()
            display.food(food_)
            display.snake(snake_)
            display.snake_length(f"Current Snake Length: {len(snake_)}")
            screen.refresh()

            if game_over.check(snake_, boundaries):
                display.game_over("Game Over. Press 'p' to play again or 'q' to quit.")
                screen.refresh()
                if game_over.restart(screen):
                    game()  # restart game
                break

            # speed of snake
            time.sleep(0.1)

    game()


if __name__ == '__main__':
    curses.wrapper(main)
