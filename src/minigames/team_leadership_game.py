import pygame
import random
from logger import logger

class TeamLeadershipGame:
    def __init__(self, screen, font, scenarios):
        self.screen = screen
        self.font = font
        self.scenarios = scenarios
        random.shuffle(self.scenarios)
        self.current_scenario = 0
        self.selected_option = None
        self.feedback = None
        self.score = 0
        self.max_score = len(scenarios) * 3  # Maximale Punktzahl pro Szenario ist 3

    def draw(self):
        self.screen.fill((255, 255, 255))
        scenario = self.scenarios[self.current_scenario]
        self.draw_text(scenario["situation"], (0, 0, 0), 50, 50)
        
        for i, option in enumerate(scenario["options"]):
            color = (0, 0, 255) if i == self.selected_option else (0, 0, 0)
            self.draw_text(f"{i+1}. {option['text']}", color, 70, 150 + i * 50)
        
        if self.feedback:
            self.draw_text(self.feedback, (0, 255, 0), 50, 350)
        
        self.draw_text(f"Scenario: {self.current_scenario + 1}/{len(self.scenarios)}", (0, 0, 0), 50, 500)
        self.draw_text(f"Score: {self.score}/{self.max_score}", (0, 0, 0), 50, 530)

    def draw_text(self, text, color, x, y):
        words = text.split()
        lines = []
        current_line = words[0]
        for word in words[1:]:
            if self.font.size(current_line + " " + word)[0] <= 700:
                current_line += " " + word
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        
        for i, line in enumerate(lines):
            surface = self.font.render(line, True, color)
            self.screen.blit(surface, (x, y + i * 30))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3] and self.feedback is None:
                self.selected_option = event.key - pygame.K_1
                self.show_feedback()
            elif event.key == pygame.K_SPACE and self.feedback:
                self.next_scenario()
        return False

    def show_feedback(self):
        option = self.scenarios[self.current_scenario]["options"][self.selected_option]
        self.score += option["score"]
        self.feedback = option["feedback"]

    def next_scenario(self):
        self.current_scenario += 1
        self.selected_option = None
        self.feedback = None
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