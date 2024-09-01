import pygame
from scenes.base_scene import BaseScene
from config import config
from npc import NPC
from quiz import Quiz
from camera import Camera
from game_objects import GameObject
from logger import logger

class GameWorldScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = self.game_engine.asset_manager.get_font('raleway', 24, 'regular')
        self.player = self.game_engine.player
        self.background = self.game_engine.asset_manager.get_sprite('tilemap')
        if self.background is None:
            logger.warning("'tilemap' sprite not found. Using a solid color background.")
            self.background = pygame.Surface((config.get('window_width'), config.get('window_height')))
            self.background.fill((100, 100, 100))
        self.npcs = self.create_npcs()
        self.objects = self.create_objects()
        self.obstacles = self.create_obstacles()
        self.current_quiz = None
        self.camera = Camera(config.get('window_width'), config.get('window_height'))
        self.camera.update(self.player)
        self.game_engine.sound_manager.play_background_music('telecom')
        self.show_instructions = True
        self.instruction_timer = 5

    def create_npcs(self):
        return [
            NPC("HR Manager", (100, 100), "Welcome! Let's discuss our company culture.", "npc1"),
            NPC("IT Specialist", (300, 200), "Need help with your tech setup?", "npc2"),
            NPC("Team Lead", (500, 300), "Let's talk about your role and responsibilities.", "npc3")
        ]

    def create_objects(self):
        return [
            GameObject(200, 200, 'book', "Company Handbook", "Contains important company policies.", self.game_engine.asset_manager),
            GameObject(400, 400, 'potion', "Coffee", "A productivity booster!", self.game_engine.asset_manager)
        ]

    def create_obstacles(self):
        return [
            pygame.Rect(50, 50, 100, 20),
            pygame.Rect(50, 50, 20, 100),
            pygame.Rect(400, 300, 150, 30),
        ]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            logger.debug(f"Key pressed: {key_name}")
            if event.key == pygame.K_SPACE:
                logger.debug("Attempting to interact")
                self.interact()
            elif event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                self.handle_movement_key(event.key)
        elif event.type == pygame.KEYUP:
            key_name = pygame.key.name(event.key)
            logger.debug(f"Key released: {key_name}")

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
        logger.debug("Attempting to interact")
        for npc in self.npcs:
            if self.player.rect.colliderect(npc.rect):
                logger.info(f"Interacting with NPC: {npc.name}")
                questions = npc.get_questions()
                from scenes.quiz import QuizScene
                self.game_engine.change_scene(QuizScene(self.game_engine, questions))
                return
        for obj in self.objects:
            if self.player.rect.colliderect(obj.rect):
                message = obj.interact(self.player)
                logger.info(message)
                self.game_engine.sound_manager.play_effect('pickup')
                self.objects.remove(obj)
                return
        logger.debug("No interaction possible")

    def update(self, dt):
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
        screen.blit(self.background, self.camera.apply_rect(pygame.Rect(0, 0, self.background.get_width(), self.background.get_height())))
        
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, (100, 100, 100), self.camera.apply_rect(obstacle))
        
        for npc in self.npcs:
            if npc.sprite:
                screen.blit(npc.sprite, self.camera.apply(npc))
            else:
                pygame.draw.rect(screen, (0, 255, 0), self.camera.apply_rect(npc.rect))
        
        for obj in self.objects:
            if obj.image:
                screen.blit(obj.image, self.camera.apply(obj))
            else:
                pygame.draw.rect(screen, (255, 0, 0), self.camera.apply_rect(obj.rect))
        
        if self.player.sprite:
            player_pos = self.camera.apply(self.player)
            screen.blit(self.player.sprite, player_pos)
            logger.debug(f"Player rendered at: {player_pos}, actual position: ({self.player.rect.x}, {self.player.rect.y})")
        else:
            logger.warning("Player sprite not found")
            pygame.draw.rect(screen, (0, 0, 255), self.camera.apply_rect(self.player.rect))
        
        info_text = self.font.render(f"Player: {self.player.name} | Level: {self.player.level} | XP: {self.player.xp}", True, (255, 255, 255))
        screen.blit(info_text, (10, 10))

        if self.current_quiz:
            self.current_quiz.render(screen)

        if self.show_instructions:
            instructions = self.font.render("Use arrow keys to move, SPACE to interact", True, (255, 255, 255))
            screen.blit(instructions, (screen.get_width() // 2 - instructions.get_width() // 2, 50))

        for x in range(0, self.background.get_width(), 50):
            pygame.draw.line(screen, (200, 200, 200), self.camera.apply_rect(pygame.Rect(x, 0, 0, self.background.get_height())).topleft, 
                             self.camera.apply_rect(pygame.Rect(x, self.background.get_height(), 0, 0)).bottomleft)
        for y in range(0, self.background.get_height(), 50):
            pygame.draw.line(screen, (200, 200, 200), self.camera.apply_rect(pygame.Rect(0, y, self.background.get_width(), 0)).topleft, 
                             self.camera.apply_rect(pygame.Rect(self.background.get_width(), y, 0, 0)).topright)

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