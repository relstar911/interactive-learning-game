import pygame
from scenes.base_scene import BaseScene
from config import config
from npc import NPC
from quiz import Quiz
from camera import Camera
from game_objects import GameObject

class GameWorldScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = self.game_engine.asset_manager.get_font('raleway', 24, 'regular')
        self.player = self.game_engine.player
        self.background = self.game_engine.asset_manager.get_sprite('tilemap')
        if self.background is None:
            print("Warnung: 'tilemap' Sprite nicht gefunden. Verwende einen einfarbigen Hintergrund.")
            self.background = pygame.Surface((config.get('window_width'), config.get('window_height')))
            self.background.fill((100, 100, 100))  # Grauer Hintergrund als Fallback
        self.npcs = self.create_npcs()
        self.objects = self.create_objects()
        self.obstacles = self.create_obstacles()
        self.current_quiz = None
        self.camera = Camera(config.get('window_width'), config.get('window_height'))
        self.camera.update(self.player)  # Initialisiere die Kamera mit der Spielerposition
        self.game_engine.sound_manager.play_background_music('telecom')
        self.show_instructions = True
        self.instruction_timer = 5  # Zeige Anweisungen für 5 Sekunden

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
            pygame.Rect(50, 50, 100, 20),   # Horizontale Wand
            pygame.Rect(50, 50, 20, 100),   # Vertikale Wand
            pygame.Rect(400, 300, 150, 30), # Größeres Hindernis
        ]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {pygame.key.name(event.key)}")  # Debugging-Ausgabe
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                self.move_player(event.key)
            elif event.key == pygame.K_SPACE:
                self.interact()

    def move_player(self, key):
        dx, dy = 0, 0
        if key == pygame.K_LEFT: dx = -1
        elif key == pygame.K_RIGHT: dx = 1
        elif key == pygame.K_UP: dy = -1
        elif key == pygame.K_DOWN: dy = 1
        
        new_x = self.player.rect.x + dx * self.player.speed
        new_y = self.player.rect.y + dy * self.player.speed
        new_rect = pygame.Rect(new_x, new_y, self.player.rect.width, self.player.rect.height)
        
        print(f"Attempting to move player to: ({new_x}, {new_y})")
        
        if not self.check_collision(new_rect):
            self.player.set_position(new_x, new_y)
            print(f"Player moved to: ({self.player.rect.x}, {self.player.rect.y})")
        else:
            print("Movement blocked by collision")

    def check_collision(self, rect):
        for obstacle in self.obstacles:
            if rect.colliderect(obstacle):
                # Erlauben Sie eine kleine Überlappung
                overlap = 5
                if (abs(rect.right - obstacle.left) < overlap or
                    abs(rect.left - obstacle.right) < overlap or
                    abs(rect.bottom - obstacle.top) < overlap or
                    abs(rect.top - obstacle.bottom) < overlap):
                    return False
                print(f"Collision detected with obstacle: {obstacle}")
                return True
        return False

    def interact(self):
        print("Attempting to interact")  # Debugging-Ausgabe
        for npc in self.npcs:
            if self.player.rect.colliderect(npc.rect):
                print(f"Interacting with NPC: {npc.name}")  # Debugging-Ausgabe
                questions = npc.get_questions()
                from scenes.quiz import QuizScene
                self.game_engine.change_scene(QuizScene(self.game_engine, questions))
                return
        for obj in self.objects:
            if self.player.rect.colliderect(obj.rect):
                message = obj.interact(self.player)
                print(message)  # In Zukunft: Nachricht auf dem Bildschirm anzeigen
                self.game_engine.sound_manager.play_effect('pickup')
                self.objects.remove(obj)
                return
        print("No interaction possible")  # Debugging-Ausgabe

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_player(pygame.K_LEFT)
        if keys[pygame.K_RIGHT]:
            self.move_player(pygame.K_RIGHT)
        if keys[pygame.K_UP]:
            self.move_player(pygame.K_UP)
        if keys[pygame.K_DOWN]:
            self.move_player(pygame.K_DOWN)

        self.camera.update(self.player)
        print(f"Player position: ({self.player.rect.x}, {self.player.rect.y})")
        print(f"Camera position: ({self.camera.camera.x}, {self.camera.camera.y})")

        # Rest der update Methode bleibt unverändert

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
            print(f"Player rendered at: {player_pos}, actual position: ({self.player.rect.x}, {self.player.rect.y})")  # Debugging-Ausgabe
        else:
            print("Warning: Player sprite not found")
            pygame.draw.rect(screen, (0, 0, 255), self.camera.apply_rect(self.player.rect))
        
        info_text = self.font.render(f"Player: {self.player.name} | Level: {self.player.level} | XP: {self.player.xp}", True, (255, 255, 255))
        screen.blit(info_text, (10, 10))

        if self.current_quiz:
            self.current_quiz.render(screen)

        if self.show_instructions:
            instructions = self.font.render("Use arrow keys to move, SPACE to interact", True, (255, 255, 255))
            screen.blit(instructions, (screen.get_width() // 2 - instructions.get_width() // 2, 50))

        # Zeichne ein Gitter, um die Bewegung zu visualisieren
        for x in range(0, self.background.get_width(), 50):
            pygame.draw.line(screen, (200, 200, 200), self.camera.apply_rect(pygame.Rect(x, 0, 0, self.background.get_height())).topleft, 
                             self.camera.apply_rect(pygame.Rect(x, self.background.get_height(), 0, 0)).bottomleft)
        for y in range(0, self.background.get_height(), 50):
            pygame.draw.line(screen, (200, 200, 200), self.camera.apply_rect(pygame.Rect(0, y, self.background.get_width(), 0)).topleft, 
                             self.camera.apply_rect(pygame.Rect(self.background.get_width(), y, 0, 0)).topright)