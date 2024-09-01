import pygame
from enum import Enum
from config import config
import traceback
from asset_manager import AssetManager
from sound_manager import SoundManager  # Importieren Sie den SoundManager
from logger import logger

class GameState(Enum):
    MAIN_MENU = 0
    CHARACTER_CREATION = 1
    TUTORIAL = 2
    GAME_WORLD = 3
    QUIZ = 4
    MINI_GAME = 5
    PAUSE = 6

class GameEngine:
    def __init__(self):
        logger.info("Initializing GameEngine")
        pygame.init()
        self.width = config.get('window_width')
        self.height = config.get('window_height')
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(config.get('window_title'))
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_scene = None
        self.player = None
        self.paused = False
        self.state = GameState.MAIN_MENU
        
        self.asset_manager = AssetManager()
        self.sound_manager = SoundManager(self.asset_manager)  # Initialisieren Sie den SoundManager
        
        logger.info(f"GameEngine initialized. Screen size: {self.width}x{self.height}")

    def change_scene(self, scene):
        logger.info(f"Changing scene to {scene.__class__.__name__}")
        self.current_scene = scene

    def change_state(self, new_state):
        self.state = new_state
        logger.info(f"Game state changed to {new_state}")

    def run(self):
        logger.info("Starting game loop")
        try:
            self.running = True
            while self.running:
                dt = self.clock.tick(config.get('fps')) / 1000.0  # Delta time in Sekunden
                self.handle_events()
                self.update(dt)
                self.render()
        except Exception as e:
            logger.error(f"An error occurred in the game loop: {str(e)}", exc_info=True)
        finally:
            logger.info("Exiting game loop")
            pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                    logger.debug(f"Game paused: {self.paused}")
                elif not self.paused and self.current_scene:
                    self.current_scene.handle_event(event)
            elif not self.paused and self.current_scene:
                self.current_scene.handle_event(event)

    def update(self, dt):
        if not self.paused and self.current_scene:
            self.current_scene.update(dt)

    def render(self):
        if self.current_scene:
            self.current_scene.render(self.screen)
            if self.paused:
                self.render_pause_screen()
            pygame.display.flip()
        else:
            logger.warning("No current scene to render")

    def render_pause_screen(self):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))
        font = self.asset_manager.get_font('raleway', 48, 'bold')
        text = font.render("PAUSED", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)

    def play_sound(self, sound_name):
        self.sound_manager.play_effect(sound_name)

game_engine = GameEngine()