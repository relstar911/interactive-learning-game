import pygame
from scenes.base_scene import BaseScene
from scenes.character_creation import CharacterCreationScene
from config import config
from logger import logger

class MainMenuScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        logger.info("Initializing MainMenuScene")
        self.font_large = self.game_engine.asset_manager.get_font('raleway', 48, 'bold')
        self.font_medium = self.game_engine.asset_manager.get_font('raleway', 32, 'regular')
        self.title = self.font_large.render(config.get('window_title'), True, (255, 255, 255))
        self.start_text = self.font_medium.render("Press SPACE to start", True, (255, 255, 255))
        self.quit_text = self.font_medium.render("Press Q to quit", True, (255, 255, 255))
        self.background = self.game_engine.asset_manager.get_sprite('tilemap')  # Annahme: Es gibt ein 'tilemap' Sprite

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                logger.info("Space key pressed, changing to CharacterCreationScene")
                self.game_engine.change_scene(CharacterCreationScene(self.game_engine))
            elif event.key == pygame.K_q:
                logger.info("Q key pressed, quitting game")
                self.game_engine.running = False

    def update(self, dt):
        pass  # Hier könnten wir Animationen oder andere Updates hinzufügen

    def render(self, screen):
        # Hintergrund zeichnen
        if self.background:
            screen.blit(self.background, (0, 0))
        else:
            screen.fill((0, 0, 0))  # Schwarzer Hintergrund als Fallback
        
        screen_width, screen_height = screen.get_size()
        
        # Titel rendern
        title_rect = self.title.get_rect(center=(screen_width // 2, screen_height // 4))
        screen.blit(self.title, title_rect)
        
        # Start-Text rendern
        start_rect = self.start_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(self.start_text, start_rect)
        
        # Quit-Text rendern
        quit_rect = self.quit_text.get_rect(center=(screen_width // 2, 3 * screen_height // 4))
        screen.blit(self.quit_text, quit_rect)

        # Kein pygame.display.flip() hier, da das in der GameEngine-Klasse gemacht wird