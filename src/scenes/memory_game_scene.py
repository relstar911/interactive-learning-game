from scenes.base_scene import BaseScene
from mini_game import MemoryGame

class MemoryGameScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.memory_game = MemoryGame(game_engine.screen, game_engine.asset_manager.get_font('raleway', 24, 'regular'))

    def handle_event(self, event):
        if self.memory_game.handle_event(event):
            self.game_engine.player.gain_xp(self.memory_game.get_score() * 5)
            from scenes.game_world_scene import GameWorldScene
            self.game_engine.change_scene(GameWorldScene(self.game_engine))

    def update(self, dt):
        self.memory_game.update(dt)

    def render(self, screen):
        self.memory_game.draw()