from scenes.base_scene import BaseScene
import pygame
from config import config
from scenes.game_world_scene import GameWorldScene

class TutorialScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font_large = self.game_engine.asset_manager.get_font('raleway', 32, 'bold')
        self.font_medium = self.game_engine.asset_manager.get_font('raleway', 24, 'regular')

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.game_engine.change_scene(GameWorldScene(self.game_engine))

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((200, 230, 250))  # Hellblauer Hintergrund
        
        title = self.font_large.render("Tutorial", True, (0, 0, 0))
        instruction = self.font_medium.render("Press ENTER to start the game", True, (0, 0, 0))
        
        screen_width, screen_height = screen.get_size()
        
        screen.blit(title, (screen_width // 2 - title.get_width() // 2, 100))
        screen.blit(instruction, (screen_width // 2 - instruction.get_width() // 2, 300))