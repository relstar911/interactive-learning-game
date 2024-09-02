import pygame
from scenes.base_scene import BaseScene
from game_states import GameState

class PauseScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = self.game_engine.asset_manager.get_font('raleway', 32, 'bold')

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game_engine.scene_manager.pop_scene()

    def update(self, dt):
        pass

    def render(self, screen):
        # Render the paused game in the background
        self.game_engine.scene_manager.scenes[GameState.GAME_WORLD].render(screen)
        
        # Add a semi-transparent overlay
        overlay = pygame.Surface((self.game_engine.width, self.game_engine.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        screen.blit(overlay, (0, 0))
        
        text = self.font.render("PAUSED", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.game_engine.width // 2, self.game_engine.height // 2))
        screen.blit(text, text_rect)