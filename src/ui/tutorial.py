import pygame

class Tutorial:
    def __init__(self):
        self.font = pygame.font.Font(None, 32)
        self.texts = [
            "Welcome to the Interactive Learning Game!",
            "Use arrow keys to move around the office.",
            "Press SPACE to interact with NPCs and objects.",
            "Learn about company culture, IT systems, and more.",
            "Complete tasks and mini-games to progress.",
            "Press ESC to exit the tutorial."
        ]
        self.current_text = 0

    def next_text(self):
        self.current_text = (self.current_text + 1) % len(self.texts)

    def render(self, screen):
        text_surface = self.font.render(self.texts[self.current_text], True, (255, 255, 255))
        screen.blit(text_surface, (50, 50))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_text()