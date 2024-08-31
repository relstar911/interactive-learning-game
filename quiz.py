import pygame
from pygame.locals import *
import random

class Quiz:
    def __init__(self, window, font):
        self.window = window
        self.font = font
        self.questions = [
            {"question": "Was ist die Hauptstadt von Deutschland?", "answers": ["Berlin", "Hamburg", "München", "Frankfurt"], "correct": 0},
            {"question": "Welches Jahr wurde Pygame veröffentlicht?", "answers": ["2000", "2005", "2010", "2015"], "correct": 0},
            {"question": "Welche Programmiersprache wird für Pygame verwendet?", "answers": ["Java", "C++", "Python", "JavaScript"], "correct": 2},
            {"question": "Was ist der Zweck von 'self' in Python-Klassen?", "answers": ["Globale Variable", "Instanzvariable", "Klassenvariable", "Lokale Variable"], "correct": 1},
            {"question": "Welche Methode wird automatisch aufgerufen, wenn ein Objekt erstellt wird?", "answers": ["__init__", "__main__", "__call__", "__new__"], "correct": 0},
        ]
        self.questions.extend([
            {"question": "Was ist ein Vorteil von Python?", "answers": ["Statische Typisierung", "Schnelle Ausführung", "Einfache Syntax", "Manuelle Speicherverwaltung"], "correct": 2},
            {"question": "Welche Datenstruktur verwendet Pygame für Rechtecke?", "answers": ["Rect", "Square", "Box", "Rectangle"], "correct": 0},
            {"question": "Was ist der Zweck der pygame.init() Funktion?", "answers": ["Spiel beenden", "Pygame initialisieren", "Fenster schließen", "Musik abspielen"], "correct": 1},
        ])
        random.shuffle(self.questions)
        self.current_question = 0
        self.score = 0

    def draw(self):
        self.window.fill((255, 255, 255))
        question = self.questions[self.current_question]
        self.draw_text(question["question"], (0, 0, 0), 100, 100)
        for i, answer in enumerate(question["answers"]):
            self.draw_text(f"{i+1}. {answer}", (0, 0, 0), 120, 200 + i * 50)
        self.draw_text(f"Score: {self.score}/{self.current_question}", (0, 0, 0), 100, 500)
        pygame.display.flip()

    def draw_text(self, text, color, x, y):
        surface = self.font.render(text, True, color)
        rect = surface.get_rect()
        rect.topleft = (x, y)
        self.window.blit(surface, rect)

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key in [K_1, K_2, K_3, K_4]:
                self.check_answer(event.key - K_1)
                self.current_question += 1
                if self.current_question >= len(self.questions):
                    return True
        return False

    def check_answer(self, answer):
        if answer == self.questions[self.current_question]["correct"]:
            self.score += 1

    def get_score(self):
        return self.score

    def reset(self):
        self.current_question = 0
        self.score = 0
        random.shuffle(self.questions)