import pygame
from scenes.base_scene import BaseScene
from player import Player
from scenes.tutorial import TutorialScene
from asset_manager import asset_manager

class CharacterCreationScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = asset_manager.get_font('main', 36)
        self.name = ""
        self.error_message = ""
        self.max_name_length = 15
        print("CharacterCreationScene initialized")

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.name:
                    print(f"Creating player with name: {self.name}")
                    player = Player(self.name, self.game_engine.width // 2, self.game_engine.height // 2)
                    self.game_engine.player = player
                    self.game_engine.change_scene(TutorialScene(self.game_engine))
                else:
                    self.error_message = "Name darf nicht leer sein!"
            elif event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
                self.error_message = ""
            elif len(self.name) < self.max_name_length:
                self.name += event.unicode
                self.error_message = ""
            else:
                self.error_message = f"Maximale Namenslänge von {self.max_name_length} erreicht!"

    def update(self, dt):
        pass  # Hier können Sie bei Bedarf Update-Logik hinzufügen

    def render(self, screen):
        print("Rendering CharacterCreationScene")
        screen.fill((255, 255, 255))
        title = self.font.render("Create Your Character", True, (0, 0, 0))
        name_prompt = self.font.render("Enter your name:", True, (0, 0, 0))
        name_text = self.font.render(self.name, True, (0, 0, 255))
        instruction = self.font.render("Press ENTER when done", True, (0, 0, 0))
        
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))
        screen.blit(name_prompt, (screen.get_width() // 2 - name_prompt.get_width() // 2, 200))
        screen.blit(name_text, (screen.get_width() // 2 - name_text.get_width() // 2, 250))
        screen.blit(instruction, (screen.get_width() // 2 - instruction.get_width() // 2, 350))

        if self.error_message:
            error_text = self.font.render(self.error_message, True, (255, 0, 0))
            screen.blit(error_text, (screen.get_width() // 2 - error_text.get_width() // 2, 400))

        name_length = self.font.render(f"Namenslänge: {len(self.name)}/{self.max_name_length}", True, (100, 100, 100))
        screen.blit(name_length, (screen.get_width() // 2 - name_length.get_width() // 2, 300))