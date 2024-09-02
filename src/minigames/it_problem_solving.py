import pygame
import random

class ITProblemSolving:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.problems = [
            {"question": "A user can't connect to the internet. What's the first step?", 
             "options": ["Check Wi-Fi connection", "Reinstall OS", "Replace computer", "Call CEO"],
             "correct": 0},
            {"question": "How do you create a strong password?", 
             "options": ["Use birthdate", "Use 'password'", "Mix letters, numbers, symbols", "Use favorite color"],
             "correct": 2},
            {"question": "What should you do if you suspect a phishing email?", 
             "options": ["Click all links", "Reply with personal info", "Delete and report", "Forward to colleagues"],
             "correct": 2},
        ]
        self.current_problem = 0
        self.score = 0
        self.game_over = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
            answer = event.key - pygame.K_1
            if answer == self.problems[self.current_problem]["correct"]:
                self.score += 1
            self.current_problem += 1
            if self.current_problem >= len(self.problems):
                self.game_over = True
        return self.game_over

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        if not self.game_over:
            problem = self.problems[self.current_problem]
            question_text = self.font.render(problem["question"], True, (0, 0, 0))
            self.screen.blit(question_text, (50, 50))
            for i, option in enumerate(problem["options"]):
                option_text = self.font.render(f"{i+1}. {option}", True, (0, 0, 0))
                self.screen.blit(option_text, (50, 100 + i * 30))
        else:
            score_text = self.font.render(f"Game Over! Your score: {self.score}/{len(self.problems)}", True, (0, 0, 0))
            self.screen.blit(score_text, (50, 50))

    def get_score(self):
        return self.score