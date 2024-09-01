import pygame
import time
from scenes.base_scene import BaseScene
from npc import NPC
from game_objects import GameObject
from content.game_content import WORLD_CONFIG, ALL_LEVELS_CONTENT, INTERACTIVE_OBJECTS, NPC_DIALOGUES
from content.game_config import LEVEL_CONFIGS
from camera import Camera
from logger import logger
from config import config

class GameWorldScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.player = self.game_engine.player
        self.tilemap = self.game_engine.asset_manager.get_sprite('tilemap')
        self.level_content = ALL_LEVELS_CONTENT[self.game_engine.current_level]
        self.npcs = self.create_npcs()
        self.objects = self.create_objects()
        self.interactive_objects = self.create_interactive_objects()
        self.obstacles = self.create_obstacles()
        self.camera = Camera(config.window_width, config.window_height)
        self.font = self.game_engine.asset_manager.get_font('raleway', 24, 'regular')
        self.current_npc = None
        self.last_interaction_time = 0
        self.show_instructions = True
        self.current_task = None  # Initialisieren Sie current_task hier

    def create_npcs(self):
        return [NPC(npc_data, self.game_engine.asset_manager) for npc_data in self.level_content["npcs"]]

    def create_objects(self):
        return [GameObject(obj["position"][0], obj["position"][1], obj["name"], obj["description"], self.game_engine.asset_manager, obj["sprite"]) for obj in self.level_content["objects"]]

    def create_interactive_objects(self):
        return [GameObject(obj["position"][0], obj["position"][1], obj["name"], obj["interaction"], self.game_engine.asset_manager, obj["sprite"]) for obj in INTERACTIVE_OBJECTS]

    def create_obstacles(self):
        return [pygame.Rect(*obstacle) for obstacle in WORLD_CONFIG["obstacle_positions"]]

    def update(self, dt):
        self.player.update(dt)
        self.camera.update(self.player)
        for npc in self.npcs:
            npc.update(dt)

    def render(self, screen):
        # Zeichnen der Tilemap
        for y in range(0, self.tilemap.get_height(), 32):
            for x in range(0, self.tilemap.get_width(), 32):
                screen.blit(self.tilemap, self.camera.apply_rect(pygame.Rect(x, y, 32, 32)), (0, 0, 32, 32))
        
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, (100, 100, 100), self.camera.apply_rect(obstacle))
        
        for npc in self.npcs:
            npc.draw(screen, self.camera)
        
        for obj in self.objects + self.interactive_objects:
            obj.draw(screen, self.camera)
        
        self.player.draw(screen, self.camera)
        
        info_text = self.font.render(f"Player: {self.player.name} | Level: {self.player.level} | XP: {self.player.xp}", True, (255, 255, 255))
        screen.blit(info_text, (10, 10))

        if self.show_instructions:
            instructions = self.font.render("Use arrow keys to move, SPACE to interact", True, (255, 255, 255))
            screen.blit(instructions, (screen.get_width() // 2 - instructions.get_width() // 2, 50))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.interact()

    def interact(self):
        current_time = time.time()
        if current_time - self.last_interaction_time < 1:  # 1 Sekunde Verzögerung
            return
        self.last_interaction_time = current_time
        
        logger.debug("Attempting to interact")
        for npc in self.npcs:
            if self.player.rect.colliderect(npc.rect):
                logger.info(f"Interacting with NPC: {npc.name}")
                dialogue = npc.interact()
                self.show_dialogue(dialogue)
                self.current_npc = npc
                return

        for obj in self.interactive_objects:
            if self.player.rect.colliderect(obj.rect):
                logger.info(f"Interacting with object: {obj.name}")
                interaction = obj.interact()
                self.show_dialogue(interaction)
                return

        logger.debug("No interaction possible")

    def show_dialogue(self, dialogue):
        # Implementieren Sie hier die Logik zum Anzeigen des Dialogs
        logger.info(f"Showing dialogue: {dialogue}")
        # Hier könnten Sie ein Dialogfenster öffnen oder den Text auf dem Bildschirm anzeigen

    def start_dialogue(self, npc):
        dialogue = NPC_DIALOGUES.get(npc.role, {})
        if not dialogue:
            logger.warning(f"No dialogue found for NPC role: {npc.role}")
            return
        self.current_dialogue = dialogue
        self.show_dialogue_options()

    def show_dialogue_options(self):
        options = self.current_dialogue.get("options", [])
        for i, option in enumerate(options):
            logger.debug(f"Dialogue option {i+1}: {option['text']}")
        # Implementieren Sie hier die Logik zum Anzeigen der Dialogoptionen

    def start_task(self, task):
        self.current_task = task

    def end_task(self):
        self.current_task = None