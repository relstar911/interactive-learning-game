import pygame
from scenes.base_scene import BaseScene
from npc import NPC
from game_objects import GameObject
from asset_manager import asset_manager

class GameWorldScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.player = self.game_engine.player
        self.background = asset_manager.get_sprite('background')
        self.npcs = [
            NPC("Tutor", (100, 100), "Willkommen im Spiel!", "tutor_sprite")
        ]
        self.game_objects = [
            GameObject(200, 200, "book", "Lehrbuch", "Ein Buch über Pygame-Programmierung."),
            GameObject(400, 400, "potion", "XP-Trank", "Gibt dir zusätzliche Erfahrungspunkte.")
        ]
        self.game_objects.extend([
            GameObject(300, 150, "potion", "Heiltrank", "Stellt Gesundheit wieder her."),
            GameObject(500, 250, "scroll", "Zauberspruchrolle", "Enthält einen mächtigen Zauber."),
            GameObject(150, 400, "coin", "Goldmünze", "Glänzende Münze mit hohem Wert.")
        ])
        self.trees = self.create_trees()
        self.font = pygame.font.Font(None, 24)
        self.message = ""
        self.message_timer = 0
        self.zones = {
            "start": pygame.Rect(0, 0, 400, 300),
            "forest": pygame.Rect(400, 0, 400, 300),
            "village": pygame.Rect(0, 300, 400, 300),
            "mountain": pygame.Rect(400, 300, 400, 300)
        }
        self.current_zone = "start"
        self.scene_change_cooldown = 500  # 500 Millisekunden Cooldown
        self.last_scene_change = 0

        # Starten Sie die Hintergrundmusik
        asset_manager.play_music('background')

    def create_trees(self):
        trees = []
        tree_positions = [(50, 50), (150, 150), (450, 100), (600, 400)]
        for pos in tree_positions:
            trees.append(GameObject(pos[0], pos[1], "tree", "Baum", "Ein schöner Baum"))
        return trees

    def load_npc_sprites(self):
        for npc in self.npcs:
            npc.load_sprite(self.game_engine.asset_manager)

    def handle_event(self, event):
        current_time = pygame.time.get_ticks()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and current_time - self.last_scene_change > self.scene_change_cooldown:
                from scenes.quiz import QuizScene
                self.game_engine.change_scene(QuizScene(self.game_engine))
                self.last_scene_change = current_time
            elif event.key == pygame.K_m and current_time - self.last_scene_change > self.scene_change_cooldown:
                from scenes.mini_game import MiniGameScene
                self.game_engine.change_scene(MiniGameScene(self.game_engine))
                self.last_scene_change = current_time
            elif event.key == pygame.K_SPACE:
                self.interact_with_objects()

    def update(self, dt):
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.player.move(dx, dy)

        for npc in self.npcs:
            npc.update(dt)

        if self.message_timer > 0:
            self.message_timer -= dt * 1000  # Convert to milliseconds
            if self.message_timer <= 0:
                self.message = ""

        self.check_zone()

    def check_zone(self):
        for zone_name, zone_rect in self.zones.items():
            if zone_rect.collidepoint(self.player.rect.center):
                if zone_name != self.current_zone:
                    self.current_zone = zone_name
                    self.message = f"Du betrittst {zone_name.capitalize()}"
                    self.message_timer = 3000
                break

    def render(self, screen):
        # Render background
        if self.background:
            screen.blit(self.background, (0, 0))
        else:
            screen.fill((100, 100, 100))  # Gray background as fallback
        
        # Render trees
        for tree in self.trees:
            tree.draw(screen)
        
        # Render game objects
        for obj in self.game_objects:
            obj.draw(screen)
        
        # Render NPCs
        for npc in self.npcs:
            npc.draw(screen)
        
        # Render player
        self.player.draw(screen)

        # Render message
        if self.message:
            text_surface = self.font.render(self.message, True, (255, 255, 255))
            pygame.draw.rect(screen, (0, 0, 0, 128), (10, 550, text_surface.get_width() + 10, 40))
            screen.blit(text_surface, (15, 555))

        # Render UI
        self.render_ui(screen)

    def interact_with_objects(self):
        for obj in self.game_objects + self.npcs:
            if self.player.rect.colliderect(obj.rect):
                if isinstance(obj, GameObject):
                    self.message = obj.interact(self.player)
                    self.message_timer = 3000  # Display message for 3 seconds
                    asset_manager.play_sound('pickup')
                    self.game_objects.remove(obj)
                elif isinstance(obj, NPC):
                    response = obj.interact("Hallo!")
                    self.message = f"{obj.name}: {response}"
                    self.message_timer = 3000  # Display message for 3 seconds
                    asset_manager.play_sound('interact')

    def render_ui(self, screen):
        # Player information
        player_info = f"Name: {self.player.name} | Level: {self.player.level} | XP: {self.player.xp}"
        text_surface = self.font.render(player_info, True, (255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0, 128), (5, 5, text_surface.get_width() + 10, 30))
        screen.blit(text_surface, (10, 10))

        # Control hints
        controls = [
            "Arrow keys: Move",
            "SPACE: Interact",
            "Q: Start Quiz",
            "M: Start Mini-game"
        ]
        for i, control in enumerate(controls):
            text_surface = self.font.render(control, True, (255, 255, 255))
            pygame.draw.rect(screen, (0, 0, 0, 128), (5, screen.get_height() - 35 * (len(controls) - i), text_surface.get_width() + 10, 30))
            screen.blit(text_surface, (10, screen.get_height() - 30 * (len(controls) - i)))