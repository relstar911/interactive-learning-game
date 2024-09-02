from src.minigames.memory_game import MemoryGame
from src.minigames.hr_quiz import HRQuiz
from src.minigames.it_problem_solving import ITProblemSolving

class Minigames:
    def __init__(self):
        self.minigames = {
            "memory": MemoryGame,
            "hr_quiz": HRQuiz,
            "it_problem_solving": ITProblemSolving,
            "default_minigame": MemoryGame
        }

    def get_minigame(self, name):
        return self.minigames.get(name, self.minigames["default_minigame"])

    # Fügen Sie hier Methoden für verschiedene Minispiele hinzu
