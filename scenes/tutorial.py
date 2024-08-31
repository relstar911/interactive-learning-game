import pygame
from scenes.base_scene import BaseScene

class TutorialScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = pygame.font.Font(None, 36)
        self.tutorial_steps = [
            "Willkommen im Tutorial!",
            "Benutze die Pfeiltasten, um dich zu bewegen.",
            "Drücke SPACE, um mit Objekten zu interagieren.",
            "Drücke Q, um ein Quiz zu starten.",
            "Drücke M, um ein Mini-Spiel zu spielen.",
            "Drücke ENTER, um fortzufahren."
        ]
        self.current_step = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.current_step += 1
            if self.current_step >= len(self.tutorial_steps):
                from scenes.game_world import GameWorldScene
                self.game_engine.change_scene(GameWorldScene(self.game_engine))

    def update(self, dt):
        pass  # Hier können Sie bei Bedarf Update-Logik hinzufügen

    def render(self, screen):
        screen.fill((255, 255, 255))
        text = self.font.render(self.tutorial_steps[self.current_step], True, (0, 0, 0))
        screen.blit(text, (100, 300))