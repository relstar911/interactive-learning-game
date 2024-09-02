import pygame
import random
from content.quiz_questions import HR_QUESTIONS

class HRQuiz:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.questions = random.sample(HR_QUESTIONS, 5)  # Select 5 random questions
        self.current_question = 0
        self.score = 0
        self.game_over = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
            answer = event.key - pygame.K_1
            if answer == self.questions[self.current_question]["correct"]:
                self.score += 1
            self.current_question += 1
            if self.current_question >= len(self.questions):
                self.game_over = True
        return self.game_over

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        if not self.game_over:
            question = self.questions[self.current_question]
            question_text = self.font.render(question["question"], True, (0, 0, 0))
            self.screen.blit(question_text, (50, 50))
            for i, option in enumerate(question["options"]):
                option_text = self.font.render(f"{i+1}. {option}", True, (0, 0, 0))
                self.screen.blit(option_text, (50, 100 + i * 30))
        else:
            score_text = self.font.render(f"Quiz Over! Your score: {self.score}/{len(self.questions)}", True, (0, 0, 0))
            self.screen.blit(score_text, (50, 50))

    def get_score(self):
        return self.score