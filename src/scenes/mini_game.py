import pygame
from src.scenes.base_scene import BaseScene

class MiniGameScene(BaseScene):
    def __init__(self, game_engine, MinigameClass):
        super().__init__(game_engine)
        self.mini_game = MinigameClass(game_engine.screen, pygame.font.Font(None, 36))
        print(f"MiniGameScene initialized with {MinigameClass.__name__}")  # Debug print

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            self.return_to_game_world()
        game_over = self.mini_game.handle_event(event)
        if game_over:
            print(f"Mini-game over. Score: {self.mini_game.get_score()}")  # Debug print
            self.return_to_game_world()

    def update(self, dt):
        self.mini_game.update(dt)

    def render(self, screen):
        self.mini_game.draw()
        font = pygame.font.Font(None, 24)
        text = font.render("Press M to return to the main game", True, (255, 255, 255))
        screen.blit(text, (10, screen.get_height() - 30))

    def return_to_game_world(self):
        print("Returning to game world")  # Debug print
        self.game_engine.scene_manager.set_scene("world")