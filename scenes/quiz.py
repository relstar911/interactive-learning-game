import pygame
from scenes.base_scene import BaseScene
from quiz import Quiz

class QuizScene(BaseScene):
    def __init__(self, game_engine, questions):
        super().__init__(game_engine)
        self.quiz = Quiz(game_engine.screen, game_engine.asset_manager.get_font('raleway', 24, 'regular'), questions)

    def handle_event(self, event):
        if self.quiz.handle_event(event):
            self.game_engine.player.gain_xp(self.quiz.get_score() * 10)
            self.return_to_game_world()

    def update(self, dt):
        result = self.quiz.update()
        if result is not None:
            self.game_engine.player.update_score(result)
            self.return_to_game_world()

    def render(self, screen):
        self.quiz.render(screen)

    def return_to_game_world(self):
        from scenes.game_world_scene import GameWorldScene
        self.game_engine.change_scene(GameWorldScene(self.game_engine))