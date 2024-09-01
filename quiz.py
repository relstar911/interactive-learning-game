import pygame
import random
from logger import logger  # Fügen Sie diese Zeile hinzu

class Quiz:
    def __init__(self, screen, font, questions):
        logger.debug("Initializing Quiz")
        self.screen = screen
        self.font = font
        self.questions = questions
        random.shuffle(self.questions)
        self.current_question = 0
        self.score = 0
        self.selected_answer = None
        self.feedback = None
        self.feedback_timer = 0
        self.total_questions = min(len(self.questions), 5)  # Begrenzen Sie die Anzahl der Fragen auf 5

    def draw(self):
        self.screen.fill((255, 255, 255))
        question = self.questions[self.current_question]
        self.draw_text(question["question"], (0, 0, 0), 50, 50)
        
        for i, option in enumerate(question["options"]):
            color = (0, 0, 255) if i == self.selected_answer else (0, 0, 0)
            self.draw_text(f"{i+1}. {option}", color, 70, 150 + i * 50)
        
        if self.feedback:
            self.draw_text(self.feedback, (0, 255, 0) if "Correct" in self.feedback else (255, 0, 0), 50, 400)
        
        self.draw_text(f"Question {self.current_question + 1}/{self.total_questions}", (0, 0, 0), 50, 500)
        self.draw_text(f"Score: {self.score}/{self.total_questions}", (0, 0, 0), 50, 530)

    def draw_text(self, text, color, x, y):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            surface = self.font.render(line, True, color)
            self.screen.blit(surface, (x, y + i * 30))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and not self.feedback:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                self.selected_answer = event.key - pygame.K_1
                self.check_answer()
        return False

    def check_answer(self):
        question = self.questions[self.current_question]
        if self.selected_answer == question["correct"]:
            self.score += 1
            self.feedback = "Correct!"
        else:
            self.feedback = f"Incorrect. The correct answer was: {question['options'][question['correct']]}"
        self.feedback_timer = 2000

    def update(self, dt):
        if self.feedback:
            self.feedback_timer -= dt
            if self.feedback_timer <= 0:
                self.feedback = None
                self.current_question += 1
                self.selected_answer = None
                if self.current_question >= self.total_questions:
                    return self.score / self.total_questions
        return None

    def render(self, screen):
        logger.debug("Rendering Quiz")
        self.draw()

    def get_score(self):
        return self.score