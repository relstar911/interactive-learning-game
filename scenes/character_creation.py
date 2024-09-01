import pygame
from scenes.base_scene import BaseScene
from player import Player
from scenes.tutorial import TutorialScene
from config import config
from scenes.game_world_scene import GameWorldScene
from logger import logger

class CharacterCreationScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.name_input = ""
        self.font_large = self.game_engine.asset_manager.get_font('raleway', 32, 'bold')
        self.font_medium = self.game_engine.asset_manager.get_font('raleway', 24, 'regular')
        if self.font_large is None or self.font_medium is None:
            logger.warning("Failed to load custom fonts in CharacterCreationScene. Using system default.")
            self.font_large = pygame.font.Font(None, 32)
            self.font_medium = pygame.font.Font(None, 24)
        self.error_message = ""
        self.max_name_length = config.get('max_player_name_length')
        logger.info("CharacterCreationScene initialized")

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.name_input:
                    print(f"Creating player with name: {self.name_input}")
                    player = Player(self.name_input, self.game_engine.asset_manager)
                    self.game_engine.player = player
                    self.game_engine.change_scene(TutorialScene(self.game_engine))
                else:
                    self.error_message = "Name darf nicht leer sein!"
            elif event.key == pygame.K_BACKSPACE:
                self.name_input = self.name_input[:-1]
                self.error_message = ""
            elif len(self.name_input) < self.max_name_length:
                self.name_input += event.unicode
                self.error_message = ""
            else:
                self.error_message = f"Maximale Namenslänge von {self.max_name_length} erreicht!"

    def update(self, dt):
        pass  # Hier können Sie bei Bedarf Update-Logik hinzufügen

    def render(self, screen):
        screen.fill((255, 255, 255))  # Weißer Hintergrund
        
        title = self.font_large.render("Create Your Character", True, (0, 0, 0))
        name_prompt = self.font_medium.render("Enter your name:", True, (0, 0, 0))
        name_text = self.font_medium.render(self.name_input, True, (0, 0, 255))
        instruction = self.font_medium.render("Press ENTER when done", True, (0, 0, 0))
        
        screen_width, screen_height = screen.get_size()
        
        screen.blit(title, (screen_width // 2 - title.get_width() // 2, 100))
        screen.blit(name_prompt, (screen_width // 2 - name_prompt.get_width() // 2, 200))
        screen.blit(name_text, (screen_width // 2 - name_text.get_width() // 2, 250))
        screen.blit(instruction, (screen_width // 2 - instruction.get_width() // 2, 350))

        if self.error_message:
            error_text = self.font_medium.render(self.error_message, True, (255, 0, 0))
            screen.blit(error_text, (screen_width // 2 - error_text.get_width() // 2, 400))

        name_length = self.font_medium.render(f"Namenslänge: {len(self.name_input)}/{self.max_name_length}", True, (100, 100, 100))
        screen.blit(name_length, (screen_width // 2 - name_length.get_width() // 2, 300))

    def create_character(self, name):
        player = Player(name, 400, 300, self.game_engine.asset_manager)
        self.game_engine.player = player
        self.game_engine.change_scene(GameWorldScene(self.game_engine))