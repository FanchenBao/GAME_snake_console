class Settings:
    """ Game settings """
    def __init__(self):
        # static settings, immutable once game starts
        self.init_snake_size: int = 10  # initial size of the snake
        self.init_speed: int = 1  # initial snake speed
        self.speed_up_factor: int = 1.5  # fold change in speed after level up
        self.lvl_up_each: int = 5  # every 5 snake size increase, level up

        # dynamic settings, mutable
        self.lvl: int = 1
        self.snake_size: int = self.init_snake_size
        self.speed: int = self.init_speed

    def lvl_up(self) -> None:
        if self.snake_size % self.lvl_up_each == 0:
            self.lvl += 1
            self.speed *= self.speed_up_factor

    def snake_size_up(self) -> None:
        self.snake_size += 1

    def score(self) -> int:
        return self.snake_size * self.lvl
