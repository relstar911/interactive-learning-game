import pygame
from scenes.base_scene import BaseScene
from game_states import GameState
from logger import logger

class TutorialScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = self.game_engine.asset_manager.get_font('raleway', 32, 'bold')
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
            self.game_engine.scene_manager.set_scene(GameState.GAME_WORLD)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((255, 255, 255))  # White background
        text = self.font.render(self.tutorial_steps[self.current_step], True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.game_engine.width // 2, self.game_engine.height // 2))
        screen.blit(text, text_rect)

        if self.current_step < len(self.tutorial_steps) - 1:
            instruction = self.font.render("Press SPACE to continue", True, (0, 0, 0))
        else:
            instruction = self.font.render("Press SPACE to start the game", True, (0, 0, 0))
        instruction_rect = instruction.get_rect(center=(self.game_engine.width // 2, self.game_engine.height - 50))
        screen.blit(instruction, instruction_rect)