import pygame
import random
from logger import logger  # Fügen Sie diese Zeile hinzu

class CompanyBingo:
    def __init__(self, screen, font, facts):
        logger.debug("Initializing CompanyBingo")
        self.screen = screen
        self.font = font
        self.facts = facts
        random.shuffle(self.facts)
        self.grid = self.facts[:16]  # 4x4 grid
        self.clicked = [False] * 16
        self.bingo = False
        self.score = 0

    def draw(self):
        self.screen.fill((255, 255, 255))
        for i in range(4):
            for j in range(4):
                index = i * 4 + j
                rect = pygame.Rect(50 + j * 175, 50 + i * 125, 170, 120)
                color = (0, 255, 0) if self.clicked[index] else (200, 200, 200)
                pygame.draw.rect(self.screen, color, rect)
                self.draw_text(self.grid[index], (0, 0, 0), rect.centerx, rect.centery, center=True)
        
        if self.bingo:
            self.draw_text("BINGO!", (255, 0, 0), 400, 550, center=True)
        
        self.draw_text(f"Score: {self.score}", (0, 0, 0), 50, 550)

    def draw_text(self, text, color, x, y, center=False):
        words = text.split()
        lines = []
        current_line = words[0]
        for word in words[1:]:
            if self.font.size(current_line + " " + word)[0] <= 160:
                current_line += " " + word
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        
        for i, line in enumerate(lines):
            surface = self.font.render(line, True, color)
            rect = surface.get_rect()
            if center:
                rect.center = (x, y + i * 20 - (len(lines) - 1) * 10)
            else:
                rect.topleft = (x, y + i * 20)
            self.screen.blit(surface, rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(16):
                rect = pygame.Rect(50 + (i % 4) * 175, 50 + (i // 4) * 125, 170, 120)
                if rect.collidepoint(event.pos):
                    self.clicked[i] = True
                    self.check_bingo()
                    return self.bingo
        return False

    def check_bingo(self):
        for i in range(4):
            if all(self.clicked[i*4:i*4+4]) or all(self.clicked[i::4]):
                self.bingo = True
                self.score = sum(self.clicked)
                return
        if all(self.clicked[0::5]) or all(self.clicked[3:15:3]):
            self.bingo = True
            self.score = sum(self.clicked)

    def update(self, dt):
        if self.bingo:
            return self.score / 16
        return None

    def render(self, screen):
        self.draw()

    def get_score(self):
        return self.score