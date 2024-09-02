import pygame
import random

class MemoryGame:
    def __init__(self, window, font):
        self.window = window
        self.font = font
        self.cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
        random.shuffle(self.cards)
        self.revealed = [False] * 16
        self.first_card = None
        self.score = 0
        self.game_over = False

    def draw(self):
        self.window.fill((255, 255, 255))
        for i in range(16):
            x = i % 4 * 100 + 150
            y = i // 4 * 100 + 100
            if self.revealed[i]:
                pygame.draw.rect(self.window, (0, 255, 0), (x, y, 80, 80))
                text = self.font.render(self.cards[i], True, (0, 0, 0))
                self.window.blit(text, (x + 30, y + 30))
            else:
                pygame.draw.rect(self.window, (200, 200, 200), (x, y, 80, 80))
        
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.window.blit(score_text, (10, 10))

        if self.game_over:
            game_over_text = self.font.render("Game Over! Press R to restart", True, (255, 0, 0))
            self.window.blit(game_over_text, (200, 500))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(16):
                card_x = i % 4 * 100 + 150
                card_y = i // 4 * 100 + 100
                rect = pygame.Rect(card_x, card_y, 80, 80)
                if rect.collidepoint(x, y) and not self.revealed[i]:
                    self.revealed[i] = True
                    if self.first_card is None:
                        self.first_card = i
                    else:
                        if self.cards[i] == self.cards[self.first_card]:
                            self.score += 1
                        else:
                            pygame.time.wait(500)
                            self.revealed[i] = False
                            self.revealed[self.first_card] = False
                        self.first_card = None
                    
                    if all(self.revealed):
                        self.game_over = True
                    
                    return False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and self.game_over:
            self.__init__(self.window, self.font)
            return False

        return self.game_over

    def get_score(self):
        return self.score

    def update(self, dt):
        # Hier können Sie Aktualisierungslogik hinzufügen, z.B. für Animationen
        pass
