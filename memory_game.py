import pygame
import random

class MemoryGame:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
        random.shuffle(self.cards)
        self.card_rects = []
        self.revealed = [False] * 16
        self.first_card = None
        self.score = 0
        self.game_over = False

        for i in range(16):
            x = (i % 4) * 100 + 50
            y = (i // 4) * 100 + 50
            self.card_rects.append(pygame.Rect(x, y, 80, 80))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(self.card_rects):
                if rect.collidepoint(event.pos) and not self.revealed[i]:
                    self.reveal_card(i)
                    return self.game_over

        return False

    def reveal_card(self, index):
        self.revealed[index] = True
        if self.first_card is None:
            self.first_card = index
        else:
            if self.cards[self.first_card] == self.cards[index]:
                self.score += 1
                if self.score == 8:
                    self.game_over = True
            else:
                pygame.time.wait(500)
                self.revealed[self.first_card] = False
                self.revealed[index] = False
            self.first_card = None

    def update(self, dt):
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        for i, rect in enumerate(self.card_rects):
            if self.revealed[i]:
                pygame.draw.rect(self.screen, (0, 255, 0), rect)
                text = self.font.render(self.cards[i], True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                self.screen.blit(text, text_rect)
            else:
                pygame.draw.rect(self.screen, (200, 200, 200), rect)

        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))

    def get_score(self):
        return self.score

    def render(self, screen):
        self.draw()