from src.scenes.base_scene import BaseScene
from src.core.quiz import Quiz
from src.scenes.game_world_scene import GameWorldScene

class QuizScene(BaseScene):
    def __init__(self, game_engine, questions):
        super().__init__(game_engine)
        self.quiz = Quiz(game_engine.screen, game_engine.asset_manager.get_font('raleway_regular', 24), questions)

    def handle_event(self, event):
        if self.quiz.handle_event(event):
            self.game_engine.player.gain_xp(self.quiz.get_score() * 10)
            self.game_engine.change_scene(GameWorldScene(self.game_engine))

    def update(self, dt):
        self.quiz.update(dt)

    def render(self, screen):
        self.quiz.render(screen)