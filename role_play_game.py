import pygame
import random
from logger import logger  # Fügen Sie diese Zeile hinzu

class RolePlayGame:
    def __init__(self, screen, font, scenarios):
        logger.debug("Initializing RolePlayGame")
        self.screen = screen
        self.font = font
        self.scenarios = scenarios
        self.current_scenario = 0
        self.selected_option = None
        self.outcome = None
        self.score = 0
        self.max_score = sum(max(option["score"] for option in scenario["options"]) for scenario in self.scenarios)

    def draw(self):
        self.screen.fill((255, 255, 255))
        scenario = self.scenarios[self.current_scenario]
        self.draw_text(scenario["situation"], (0, 0, 0), 50, 50)
        
        for i, option in enumerate(scenario["options"]):
            color = (0, 0, 255) if i == self.selected_option else (0, 0, 0)
            self.draw_text(f"{i+1}. {option['text']}", color, 70, 150 + i * 50)
        
        if self.outcome:
            self.draw_text(self.outcome, (0, 255, 0), 50, 400)
        
        self.draw_text(f"Score: {self.score}/{self.max_score}", (0, 0, 0), 50, 500)

    def draw_text(self, text, color, x, y):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            surface = self.font.render(line, True, color)
            self.screen.blit(surface, (x, y + i * 30))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3] and self.outcome is None:
                self.selected_option = event.key - pygame.K_1
                self.show_outcome()
            elif event.key == pygame.K_SPACE and self.outcome:
                self.next_scenario()
        return False

    def show_outcome(self):
        option = self.scenarios[self.current_scenario]["options"][self.selected_option]
        self.outcome = option["outcome"]
        self.score += option["score"]

    def next_scenario(self):
        self.current_scenario += 1
        self.selected_option = None
        self.outcome = None
        if self.current_scenario >= len(self.scenarios):
            return True
        return False

    def update(self, dt):
        if self.current_scenario >= len(self.scenarios):
            return self.score / self.max_score
        return None

    def render(self, screen):
        self.draw()

    def get_score(self):
        return self.score