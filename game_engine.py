import pygame
from config import config

class GameEngine:
    def __init__(self):
        pygame.init()
        self.width = config.get('window.width', 800)
        self.height = config.get('window.height', 600)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(config.get('window.title', 'Interactive Learning Game'))
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_scene = None
        self.player = None
        self.paused = False
        print(f"GameEngine initialized. Screen size: {self.width}x{self.height}")

    def change_scene(self, scene):
        print(f"Changing scene to {scene.__class__.__name__}")
        self.current_scene = scene

    def run(self):
        print("Starting game loop")
        while self.running:
            dt = self.clock.tick(config.get('game.fps', 60)) / 1000.0
            self.handle_events()
            self.update(dt)
            self.render()
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.paused = not self.paused
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
        else:
            print("No current scene to render")

    def render_pause_screen(self):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))
        font = pygame.font.Font(None, 48)
        text = font.render("PAUSE", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)

game_engine = GameEngine()