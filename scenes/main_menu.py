import pygame
from scenes.base_scene import BaseScene
from scenes.character_creation import CharacterCreationScene
from asset_manager import asset_manager

class MainMenuScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = asset_manager.fonts.get('main', pygame.font.Font(None, 36))
        self.background = asset_manager.sprites.get('background')
        self.prototype_tiles = asset_manager.sprites.get('prototype_tiles')
        print(f"MainMenuScene initialized. Font: {self.font}, Background: {self.background}")

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            print("ENTER key pressed, changing to CharacterCreationScene")
            self.game_engine.change_scene(CharacterCreationScene(self.game_engine))

    def update(self, dt):
        pass  # Hier können Sie bei Bedarf Update-Logik hinzufügen

    def render(self, screen):
        print("Rendering MainMenuScene")
        if self.background:
            screen.blit(self.background, (0, 0))
        else:
            screen.fill((255, 255, 255))  # Weißer Hintergrund als Fallback
        
        # Verwenden Sie die neuen Prototype-Tiles als dekorative Elemente
        if self.prototype_tiles:
            for i in range(0, screen.get_width(), 64):
                screen.blit(self.prototype_tiles, (i, 0), (0, 0, 64, 64))  # Obere Kante
                screen.blit(self.prototype_tiles, (i, screen.get_height() - 64), (0, 0, 64, 64))  # Untere Kante

        title = self.font.render("Interactive Learning Game", True, (0, 0, 0))
        start = self.font.render("Press ENTER to start", True, (0, 0, 0))
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 200))
        screen.blit(start, (screen.get_width() // 2 - start.get_width() // 2, 300))
        print("MainMenuScene rendered")