import pygame
from scenes.base_scene import BaseScene
from game_states import GameState

class MiniGameScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = self.game_engine.asset_manager.get_font('raleway', 32, 'bold')

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game_engine.scene_manager.set_scene(GameState.GAME_WORLD)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((200, 200, 200))  # Light gray background
        text = self.font.render("Mini Game Scene", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.game_engine.width // 2, self.game_engine.height // 2))
        screen.blit(text, text_rect)