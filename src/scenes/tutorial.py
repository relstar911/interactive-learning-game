import pygame
from scenes.base_scene import BaseScene
from scenes.game_world_scene import GameWorldScene
from logger import logger

class TutorialScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font_large = self.game_engine.asset_manager.get_font('raleway', 32, 'bold')
        self.font_medium = self.game_engine.asset_manager.get_font('raleway', 24, 'regular')
        if self.font_large is None or self.font_medium is None:
            logger.warning("Failed to load custom fonts in TutorialScene. Using system default.")
            self.font_large = pygame.font.Font(None, 32)
            self.font_medium = pygame.font.Font(None, 24)
        self.tutorial_steps = [
            "Welcome to the company! Let's go through a quick tutorial.",
            "Use the arrow keys to move around.",
            "Press SPACE to interact with NPCs and objects.",
            "Complete tasks and quizzes to gain experience and level up.",
            "Press ESC to open the menu at any time.",
            "That's it! You're ready to start your journey. Good luck!"
        ]
        self.current_step = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_step()

    def next_step(self):
        self.current_step += 1
        if self.current_step >= len(self.tutorial_steps):
            self.game_engine.change_scene(GameWorldScene(self.game_engine))

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((255, 255, 255))
        title = self.font_large.render("Tutorial", True, (0, 0, 0))
        screen.blit(title, (400 - title.get_width() // 2, 50))

        text = self.font_medium.render(self.tutorial_steps[self.current_step], True, (0, 0, 0))
        screen.blit(text, (400 - text.get_width() // 2, 300))

        if self.current_step < len(self.tutorial_steps) - 1:
            instruction = self.font_medium.render("Press SPACE to continue", True, (0, 0, 0))
        else:
            instruction = self.font_medium.render("Press SPACE to start the game", True, (0, 0, 0))
        screen.blit(instruction, (400 - instruction.get_width() // 2, 500))