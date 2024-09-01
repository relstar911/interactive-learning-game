import pygame
from enum import Enum
from config import config
import traceback
from asset_manager import AssetManager
from sound_manager import SoundManager  # Importieren Sie den SoundManager
from logger import logger
from scenes.game_world_scene import GameWorldScene  # Importieren der GameWorldScene-Klasse
from game_tasks import GameTasks
from constants import SOUNDS_DIR
import os
from content.game_content import ALL_LEVELS_CONTENT
from minigames import MinigameManager

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
        
        try:
            start_music_path = os.path.join(SOUNDS_DIR, "1354018_288-Autograph-Piano-2023.mp3")
            self.start_music = self.sound_manager.load_sound(start_music_path)
            if self.start_music:
                pygame.mixer.music.load(start_music_path)
                pygame.mixer.music.play(-1)  # Endlosschleife
                logger.info("Start music playing")
            else:
                logger.error("Failed to load start music")
        except FileNotFoundError:
            logger.error("Start music file not found. Please check the path.")
            self.start_music = None
        
        logger.info(f"GameEngine initialized. Screen size: {self.width}x{self.height}")
        self.dialogue_active = False
        self.current_npc = None
        self.current_level = 1
        self.max_levels = len(ALL_LEVELS_CONTENT)
        self.minigame_manager = MinigameManager(self)

    def handle_events(self):
        for event in pygame.event.get():
            logger.debug(f"Event detected: {event}")
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                logger.debug(f"Key down: {pygame.key.name(event.key)}")
                if event.key == pygame.K_ESCAPE:
                    if isinstance(self.current_scene, GameWorldScene) and self.current_scene.current_task:
                        logger.debug("Exiting current task")
                        self.current_scene.current_task = None
                    elif self.paused:
                        self.paused = False
                        logger.debug("Unpausing game")
                    else:
                        self.paused = True
                        logger.debug("Pausing game")
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
                    logger.debug(f"Game paused: {self.paused}")
                elif not self.paused and self.current_scene:
                    self.current_scene.handle_event(event)
            elif not self.paused and self.current_scene:
                self.current_scene.handle_event(event)

        # Erfassen der Bewegung des Spielers
        keys = pygame.key.get_pressed()
        if not self.paused and self.player and isinstance(self.current_scene, GameWorldScene):
            if keys[pygame.K_LEFT]:
                self.player.move(-1, 0)
            if keys[pygame.K_RIGHT]:
                self.player.move(1, 0)
            if keys[pygame.K_UP]:
                self.player.move(0, -1)
            if keys[pygame.K_DOWN]:
                self.player.move(0, 1)

    def change_scene(self, scene):
        logger.info(f"Changing scene to {scene.__class__.__name__}")
        self.current_scene = scene
        if isinstance(scene, GameWorldScene):
            self.stop_music()
            self.play_game_music()

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

    def update(self, dt):
        if self.minigame_manager.current_game:
            result = self.minigame_manager.update(dt)
            if result is not None:
                self.player.gain_xp(result * 10)
                self.minigame_manager.end_game()
        elif self.current_scene:
            self.current_scene.update(dt)
        self.check_npc_interaction()

    def render(self):
        if self.minigame_manager.current_game:
            self.minigame_manager.render(self.screen)
        elif self.current_scene:
            self.current_scene.render(self.screen)
            if self.dialogue_active and self.current_npc:
                self.display_dialogue(self.current_npc.dialogue)
            if self.paused:
                self.render_pause_screen()
            pygame.display.flip()
        else:
            logger.warning("No current scene to render")

    def display_dialogue(self, dialogue):
        if isinstance(dialogue, dict):
            dialogue_text = dialogue.get("greeting", "No dialogue available.")
        elif isinstance(dialogue, str):
            dialogue_text = dialogue
        else:
            dialogue_text = "No dialogue available."
        
        font = self.asset_manager.get_font('raleway', 24, 'regular')
        text = font.render(dialogue_text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height - 50))
        self.screen.blit(text, text_rect)

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

    def play_start_music(self):
        try:
            pygame.mixer.music.load(os.path.join(SOUNDS_DIR, "1354018_288-Autograph-Piano-2023.mp3"))
            pygame.mixer.music.play(-1)  # Endlosschleife
            logger.info("Start music playing")
        except FileNotFoundError:
            logger.error("Start music file not found. Please check the path.")

    def play_game_music(self):
        try:
            game_music_path = os.path.join(SOUNDS_DIR, "1350180_TeleCom-INC.mp3")
            pygame.mixer.music.load(game_music_path)
            pygame.mixer.music.play(-1)  # Endlosschleife
            logger.info("Game music playing")
        except FileNotFoundError:
            logger.error("Game music file not found. Please check the path.")

    def stop_music(self):
        pygame.mixer.music.stop()
        logger.info("Music stopped")

    def check_npc_interaction(self):
        if hasattr(self.current_scene, 'npcs'):
            for npc in self.current_scene.npcs:
                if self.player.rect.colliderect(npc.rect):
                    self.dialogue_active = True
                    self.current_npc = npc
                    break
            else:
                self.dialogue_active = False
                self.current_npc = None

    def load_level(self, level):
        self.current_level = level
        level_content = ALL_LEVELS_CONTENT[level]
        # Hier würden Sie die Spielwelt mit den Level-Inhalten initialisieren
        # z.B. NPCs erstellen, Objekte platzieren, etc.
        logger.info(f"Loading level {level}")
        logger.debug(f"Level content: {level_content}")

    def next_level(self):
        if self.current_level < self.max_levels:
            self.current_level += 1
            self.load_level(self.current_level)
        else:
            logger.info("Game completed!")
            # Hier könnten Sie einen Game-Over-Zustand auslösen

game_engine = GameEngine()