import pygame
import logging
from src.core.scene_manager import SceneManager
from src.core.asset_manager import AssetManager
from src.core.input_handler import InputHandler

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.scene_manager = SceneManager()
        self.asset_manager = AssetManager()
        self.input_handler = InputHandler()
        self.running = True
        self.logger = logging.getLogger('InteractiveLearningGame')

    def run(self):
        self.logger.info("Starting game loop")
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.logger.debug(f"Frame time: {dt:.3f}s")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.logger.info("Quit event received")
                    self.running = False
                self.input_handler.handle_event(event)
                self.scene_manager.handle_event(event)
            self.scene_manager.update(dt)
            self.scene_manager.render(self.screen)
            pygame.display.flip()
        self.logger.info("Game loop ended")
        pygame.quit()

    def quit(self):
        self.logger.info("Quit method called")
        self.running = False