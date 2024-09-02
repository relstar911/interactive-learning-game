import pygame
from src.scenes.base_scene import BaseScene
from game_states import GameState

class GameWorldScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = self.game_engine.asset_manager.get_font('raleway', 32, 'bold')

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((100, 200, 100))  # Light green background
        text = self.font.render("Game World", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.game_engine.width // 2, self.game_engine.height // 2))
        screen.blit(text, text_rect)

    def init_level(self, level_content):
        # Initialize the level with the provided content
        pass