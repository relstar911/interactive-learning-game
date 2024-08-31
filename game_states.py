from enum import Enum

class GameState(Enum):
    MAIN_MENU = 0
    CHARACTER_CREATION = 1
    TUTORIAL = 2
    GAME_WORLD = 3
    QUIZ = 4
    MINI_GAME = 5
    PAUSE = 6