import pygame
from scenes.base_scene import BaseScene
from config import config
from npc import NPC
from quiz import Quiz
from camera import Camera
from game_objects import GameObject
from logger import logger
from game_tasks import GameTasks
import time
from content.game_content import (
    ALL_LEVELS_CONTENT,
    NPC_DIALOGUES,
    ONBOARDING_PROGRESS,
    MINIGAME_REWARDS,
    HR_QUESTIONS,
    IT_SCENARIOS,
    TEAM_LEAD_SCENARIOS
)
from minigames import MinigameManager
from content.asset_config import SPRITE_MAPPINGS

class GameWorldScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = self.game_engine.asset_manager.get_font('raleway', 24, 'regular')
        self.player = self.game_engine.player
        self.tilemap = self.game_engine.asset_manager.get_sprite('tilemap')
        if self.tilemap is None:
            logger.warning("'tilemap' sprite not found. Using a solid color background.")
            self.tilemap = pygame.Surface((config.get('window_width'), config.get('window_height')))
            self.tilemap.fill((100, 100, 100))
        self.level_content = ALL_LEVELS_CONTENT[self.game_engine.current_level]
        self.npcs = self.create_npcs()
        self.objects = self.create_objects()
        self.obstacles = self.create_obstacles()
        self.current_task = None
        self.camera = Camera(config.get('window_width'), config.get('window_height'))
        self.camera.update(self.player)
        self.game_engine.play_game_music()
        self.show_instructions = True
        self.instruction_timer = 5
        self.game_tasks = GameTasks(game_engine)
        self.last_interaction_time = 0
        self.current_dialogue = None
        self.current_npc = None
        self.minigame_manager = MinigameManager(game_engine)
        self.current_minigame = None

    def create_npcs(self):
        return [NPC(npc_data, self.game_engine.asset_manager) for npc_data in self.level_content["npcs"]]

    def create_objects(self):
        return [GameObject(obj["position"][0], obj["position"][1], obj["name"], obj["description"], self.game_engine.asset_manager, obj["sprite"]) for obj in self.level_content["objects"]]

    def create_obstacles(self):
        return [pygame.Rect(*obstacle) for obstacle in self.level_content["obstacle_positions"]]

    def handle_event(self, event):
        logger.debug(f"GameWorldScene handling event: {event}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.interact()
            elif event.key == pygame.K_ESCAPE:
                if self.current_task:
                    self.current_task = None
                    logger.debug("Exiting current task")
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                self.handle_movement_key(event.key)
        elif event.type == pygame.KEYUP:
            key_name = pygame.key.name(event.key)
            logger.debug(f"Key released: {key_name}")

        if self.current_task:
            self.current_task.handle_event(event)

    def handle_movement_key(self, key):
        dx, dy = 0, 0
        if key == pygame.K_LEFT:
            dx = -1
        elif key == pygame.K_RIGHT:
            dx = 1
        elif key == pygame.K_UP:
            dy = -1
        elif key == pygame.K_DOWN:
            dy = 1
        
        if dx != 0 or dy != 0:
            logger.debug(f"Moving player: dx={dx}, dy={dy}")
            self.move_player(dx, dy)

    def move_player(self, dx, dy):
        new_x = self.player.rect.x + dx * self.player.speed
        new_y = self.player.rect.y + dy * self.player.speed
        new_rect = pygame.Rect(new_x, new_y, self.player.rect.width, self.player.rect.height)
        
        logger.debug(f"Attempting to move player to: ({new_x}, {new_y})")
        
        if not self.check_collision(new_rect):
            self.player.move(dx, dy)
            logger.debug(f"Player moved to: ({self.player.rect.x}, {self.player.rect.y})")
        else:
            logger.debug("Movement blocked by collision")

    def check_collision(self, rect):
        for obstacle in self.obstacles:
            if rect.colliderect(obstacle):
                overlap = 5
                if (abs(rect.right - obstacle.left) < overlap or
                    abs(rect.left - obstacle.right) < overlap or
                    abs(rect.bottom - obstacle.top) < overlap or
                    abs(rect.top - obstacle.bottom) < overlap):
                    return False
                logger.debug(f"Collision detected with obstacle: {obstacle}")
                return True
        return False

    def interact(self):
        current_time = time.time()
        if current_time - self.last_interaction_time < 1:  # 1 Sekunde Verzögerung
            return
        self.last_interaction_time = current_time
        
        logger.debug("Attempting to interact")
        for npc in self.npcs:
            if self.player.rect.colliderect(npc.rect):
                logger.info(f"Interacting with NPC: {npc.name}")
                dialogue = npc.interact(self.game_tasks)
                self.show_dialogue(dialogue)
                self.current_npc = npc
                self.start_minigame(npc.role)
                return
        for obj in self.objects:
            if isinstance(obj, GameObject) and self.player.rect.colliderect(obj.rect):
                self.interact_with_object(obj)
                return
        logger.debug("No interaction possible")

    def interact_with_object(self, obj):
        logger.info(f"Interacting with object: {obj.name}")
        # Zeige Informationen an und aktualisiere den Fortschritt
        self.show_object_info(obj)
        self.update_progress(obj.name)

    def show_object_info(self, obj):
        # Implementieren Sie hier die Logik zum Anzeigen von Objektinformationen
        pass

    def show_dialogue(self, dialogue):
        # Implementieren Sie hier die Logik zum Anzeigen des Dialogs
        logger.info(f"Showing dialogue: {dialogue}")
        # Hier könnten Sie ein Dialogfenster öffnen oder den Text auf dem Bildschirm anzeigen

    def start_dialogue(self, npc):
        dialogue = NPC_DIALOGUES.get(npc.name)
        if not dialogue:
            logger.warning(f"No dialogue found for NPC: {npc.name}")
            return
        self.current_dialogue = dialogue
        self.show_dialogue_options()

    def show_dialogue_options(self):
        options = self.current_dialogue.get("options", [])
        for i, option in enumerate(options):
            logger.debug(f"Dialogue option {i+1}: {option['text']}")
        # Implementieren Sie hier die Logik zum Anzeigen der Dialogoptionen

    def handle_dialogue_choice(self, choice):
        options = self.current_dialogue.get("options", [])
        if 0 <= choice < len(options):
            selected_option = options[choice]
            logger.info(f"Player chose: {selected_option['text']}")
            if selected_option.get("start_game", False):
                self.start_minigame(self.current_npc.name)
            elif "follow_up" in selected_option:
                self.show_follow_up_options(selected_option["follow_up"])
            else:
                self.show_response(selected_option['response'])
                self.update_progress(self.current_npc.name)

    def show_follow_up_options(self, follow_up_options):
        # Implementieren Sie hier die Logik zum Anzeigen der Follow-up-Optionen
        pass

    def start_minigame(self, npc_role):
        if npc_role == "HR Manager":
            self.current_minigame = self.minigame_manager.start_game("quiz", HR_QUESTIONS)
        elif npc_role == "IT Specialist":
            self.current_minigame = self.minigame_manager.start_game("role_play", IT_SCENARIOS)
        elif npc_role == "Team Lead":
            self.current_minigame = self.minigame_manager.start_game("team_leadership", TEAM_LEAD_SCENARIOS)

    def update_progress(self, category):
        if category in ONBOARDING_PROGRESS:
            self.player.update_onboarding_progress(category, 1)
            logger.info(f"Updated progress for {category}: {self.player.onboarding_progress[category]}/{ONBOARDING_PROGRESS[category]['max_score']}")

    def complete_minigame(self, game_name, score):
        reward = MINIGAME_REWARDS.get(game_name)
        if reward:
            self.player.gain_xp(reward["xp"])
            self.player.add_to_inventory(reward["item"])
            logger.info(f"Player completed {game_name}. Rewarded with {reward['xp']} XP and {reward['item']}.")

    def update(self, dt):
        if self.current_minigame:
            result = self.current_minigame.update(dt)
            if result is not None:
                logger.debug(f"Task result: {result}")
                self.player.gain_xp(result * 10)
                self.current_minigame = None
        else:
            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if keys[pygame.K_LEFT]:
                dx = -1
                logger.debug("Left key pressed")
            if keys[pygame.K_RIGHT]:
                dx = 1
                logger.debug("Right key pressed")
            if keys[pygame.K_UP]:
                dy = -1
                logger.debug("Up key pressed")
            if keys[pygame.K_DOWN]:
                dy = 1
                logger.debug("Down key pressed")
            
            if dx != 0 or dy != 0:
                self.move_player(dx, dy)
                logger.debug(f"Player moved: dx={dx}, dy={dy}")

            self.camera.update(self.player)
            logger.debug(f"Player position: ({self.player.rect.x}, {self.player.rect.y})")
            logger.debug(f"Camera position: ({self.camera.camera.x}, {self.camera.camera.y})")

    def render(self, screen):
        if self.current_minigame:
            self.current_minigame.render(screen)
            # Hinzufügen eines "Zurück"-Buttons
            font = self.game_engine.asset_manager.get_font('raleway', 24, 'regular')
            back_text = font.render("Press ESC to return to map", True, (255, 255, 255))
            screen.blit(back_text, (10, screen.get_height() - 40))
        else:
            # Zeichnen der Tilemap
            for y in range(0, self.tilemap.get_height(), 32):  # Angenommen, jede Kachel ist 32x32 Pixel
                for x in range(0, self.tilemap.get_width(), 32):
                    screen.blit(self.tilemap, self.camera.apply_rect(pygame.Rect(x, y, 32, 32)), (0, 0, 32, 32))
            
            for obstacle in self.obstacles:
                pygame.draw.rect(screen, (100, 100, 100), self.camera.apply_rect(obstacle))
            
            for npc in self.npcs:
                npc.draw(screen, self.camera)
            
            for obj in self.objects:
                obj.draw(screen, self.camera)
            
            self.player.draw(screen)
            
            info_text = self.font.render(f"Player: {self.player.name} | Level: {self.player.level} | XP: {self.player.xp}", True, (255, 255, 255))
            screen.blit(info_text, (10, 10))

            if self.show_instructions:
                instructions = self.font.render("Use arrow keys to move, SPACE to interact", True, (255, 255, 255))
                screen.blit(instructions, (screen.get_width() // 2 - instructions.get_width() // 2, 50))

    def open_inventory(self):
        logger.info("Opening inventory")
        # Implementieren Sie hier die Logik zum Öffnen des Inventars
        # Zum Beispiel: self.game_engine.change_scene(InventoryScene(self.game_engine))

    def open_map(self):
        logger.info("Opening map")
        # Implementieren Sie hier die Logik zum Öffnen der Karte
        # Zum Beispiel: self.game_engine.change_scene(MapScene(self.game_engine))

    def open_quest_log(self):
        logger.info("Opening quest log")
        # Implementieren Sie hier die Logik zum Öffnen des Questlogs
        # Zum Beispiel: self.game_engine.change_scene(QuestLogScene(self.game_engine))

    def open_pause_menu(self):
        logger.info("Opening pause menu")
        # Implementieren Sie hier die Logik zum Öffnen des Pausemenüs
        self.game_engine.paused = True

    def handle_mouse_click(self, pos, button):
        logger.info(f"Mouse click handled at position {pos} with button {button}")
        # Implementieren Sie hier die Logik für Mausklicks
        # Zum Beispiel: Interaktion mit Objekten oder NPCs basierend auf der Klickposition