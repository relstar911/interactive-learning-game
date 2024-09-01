import pygame
from pygame.locals import *
import random

class Quiz:
    def __init__(self, window, font, questions):
        self.window = window
        self.font = font
        self.questions = questions
        random.shuffle(self.questions)
        self.current_question = 0
        self.score = 0
        self.selected_answer = None

    def draw(self):
        self.window.fill((255, 255, 255))
        question = self.questions[self.current_question]
        self.draw_text(question["question"], (0, 0, 0), 100, 100)
        for i, option in enumerate(question["options"]):  # Ändern Sie "answers" zu "options"
            color = (0, 0, 0) if i != self.selected_answer else (0, 0, 255)
            self.draw_text(f"{i+1}. {option}", color, 120, 200 + i * 50)
        self.draw_text(f"Score: {self.score}/{self.current_question}", (0, 0, 0), 100, 500)

    def draw_text(self, text, color, x, y):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect()
        rect.topleft = (x, y)
        self.window.blit(surface, rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                self.selected_answer = event.key - pygame.K_1
            elif event.key == pygame.K_RETURN and self.selected_answer is not None:
                correct = self.selected_answer == self.questions[self.current_question]["correct"]
                if correct:
                    self.score += 1
                self.current_question += 1
                self.selected_answer = None
                if self.current_question >= len(self.questions):
                    return True
        return False

    def update(self):
        if self.current_question >= len(self.questions):
            return self.score / len(self.questions)
        return None

    def render(self, screen):
        self.draw()