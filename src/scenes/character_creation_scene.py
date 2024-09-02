import pygame
from scenes.base_scene import BaseScene
from player import Player
from game_states import GameState
from logger import logger

class CharacterCreationScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.name_input = ""
        self.font = self.game_engine.asset_manager.get_font('raleway', 32, 'bold')
        self.error_message = ""
        self.max_name_length = 20  # Sie können dies anpassen

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.name_input:
                    self.create_character(self.name_input)
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
        pass

    def render(self, screen):
        screen.fill((255, 255, 255))  # Weißer Hintergrund
        
        title = self.font.render("Create Your Character", True, (0, 0, 0))
        name_prompt = self.font.render("Enter your name:", True, (0, 0, 0))
        name_text = self.font.render(self.name_input, True, (0, 0, 255))
        instruction = self.font.render("Press ENTER when done", True, (0, 0, 0))
        
        screen_width, screen_height = screen.get_size()
        
        screen.blit(title, (screen_width // 2 - title.get_width() // 2, 100))
        screen.blit(name_prompt, (screen_width // 2 - name_prompt.get_width() // 2, 200))
        screen.blit(name_text, (screen_width // 2 - name_text.get_width() // 2, 250))
        screen.blit(instruction, (screen_width // 2 - instruction.get_width() // 2, 350))

        if self.error_message:
            error_text = self.font.render(self.error_message, True, (255, 0, 0))
            screen.blit(error_text, (screen_width // 2 - error_text.get_width() // 2, 400))

    def create_character(self, name):
        logger.info(f"Creating player with name: {name}")
        player = Player(name, self.game_engine.asset_manager)
        self.game_engine.player = player
        self.game_engine.scene_manager.set_scene(GameState.TUTORIAL)