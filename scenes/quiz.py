import pygame
from scenes.base_scene import BaseScene
from quiz import Quiz

class QuizScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.quiz = Quiz(game_engine.screen, pygame.font.Font(None, 36))

    def handle_event(self, event):
        if self.quiz.handle_event(event):
            self.game_engine.player.gain_xp(self.quiz.get_score() * 10)
            from scenes.game_world import GameWorldScene
            self.game_engine.change_scene(GameWorldScene(self.game_engine))

    def update(self, dt):
        pass  # Hier können Sie bei Bedarf Update-Logik hinzufügen

    def render(self, screen):
        self.quiz.draw()