# Introduction
This is my second attmept at making the **snake** game. This time, I followed the lead from [Python Guide for Print](https://realpython.com/python-print/) to implement the game completely on console, using the built-in `curses` module.

The game supports the most basic functionalities for game play, including moving the snake, eating food, growing in length, and dying if snake head hits its own body or wall.

A crude scoring system is included and current score displayed on the upper right corner of the game display. However, high score is not recorded.

Upon game over, a simple message is shown on the upper left corner of the game display, letting the player choose either to play again or quit the game.

# Game Demo
![GAME_snake_console demo](https://media.giphy.com/media/ZFEEKtUkBJj2CZqA6y/giphy.gif "GAME_snake_console demo")

# Usage
* Clone this repo: `git clone https://github.com/FanchenBao/GAME_snake_console.git`
* Move to the repo folder: `cd GAME_snake_console`
* Run command: `python3 main.py`

# High Score
Highest score I have achieved so far is `450`