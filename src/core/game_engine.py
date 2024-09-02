import pygame
from src.core.sound_manager import SoundManager
from src.utils.logger import logger
from src.core.game_states import GameState
from src.core.game_tasks import GameTasks
from src.core.minigames import Minigames
from src.core.scene_manager import SceneManager
from src.core.asset_manager import AssetManager
from src.core.input_handler import InputHandler
from src.scenes.world_scene import WorldScene
from src.scenes.mini_game import MiniGameScene
from src.scenes.quiz_scene import QuizScene
from content.quiz_questions import HR_QUESTIONS, IT_QUESTIONS

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.scene_manager = SceneManager()
        self.asset_manager = AssetManager()
        self.input_handler = InputHandler()
        self.sound_manager = SoundManager()
        self.game_tasks = GameTasks()
        self.minigames = Minigames()
        self.running = True
        self.scene_manager.add_scene("world", WorldScene(self))
        self.scene_manager.add_scene("mini_game", lambda: MiniGameScene(self, self.minigames.get_minigame("memory")))
        self.scene_manager.add_scene("hr_quiz", lambda: QuizScene(self, HR_QUESTIONS))
        self.scene_manager.add_scene("it_quiz", lambda: QuizScene(self, IT_QUESTIONS))
        self.scene_manager.set_scene("world")

    def run(self):
        logger.info("Starting game loop")
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.update(dt)
            self.render()
        logger.info("Game loop ended")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.input_handler.handle_event(event)
            self.scene_manager.handle_event(event)

    def update(self, dt):
        self.scene_manager.update(dt)
        self.game_tasks.update()

    def render(self):
        self.scene_manager.render(self.screen)
        pygame.display.flip()

    def quit(self):
        self.running = False