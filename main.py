import curses
import time

# custom import
from boundaries import Boundaries
import snake
import food
from display import Display
import game_over
from settings import Settings


def main(screen):
    def game() -> None:
        curses.curs_set(0)  # hide cursor
        screen.nodelay(True)  # Don't block I/O calls

        settings = Settings()  # game settings
        boundaries = Boundaries()  # boundaries, within which snakes can move
        snake_ = snake.initialize(boundaries, settings.init_snake_size)  # initialize snake
        food_ = food.create(boundaries, snake_)  # initial food
        display = Display(boundaries, screen)  # initialize display

        directions = {
            curses.KEY_UP: (-1, 0),
            curses.KEY_DOWN: (1, 0),
            curses.KEY_LEFT: (0, -2),  # hori need to scale up to match vert
            curses.KEY_RIGHT: (0, 2),
        }
        direction = directions[curses.KEY_RIGHT]  # default direction

        while True:  # game loop
            screen.erase()

            # check whether snake has eaten the food
            eaten = snake.eat_food(snake_, food_)
            if eaten:
                food_ = food.create(boundaries, snake_)
                settings.snake_size_up()
                settings.lvl_up()

            # get direction from user arrow key input
            direction = directions.get(screen.getch(), direction)
            # move snake accordingly
            snake_ = snake.move(snake_, direction, eaten)

            # display game elements
            display.boundaries()
            display.food(food_)
            display.snake(snake_)
            display.score(f"Current score: {settings.score()}")
            screen.refresh()

            if game_over.check(snake_, boundaries):
                display.game_over("Game Over. Press 'p' to play again or 'q' to quit.")
                screen.refresh()
                if game_over.restart(screen):
                    game()  # restart game
                break

            # speed of snake
            time.sleep(0.1 / settings.speed)

    game()


if __name__ == '__main__':
    curses.wrapper(main)
