import pygame
import random

class PuzzleGame:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.puzzle_size = 3
        self.tile_size = 100
        self.puzzle = self.generate_puzzle()
        self.empty_tile = (self.puzzle_size - 1, self.puzzle_size - 1)
        self.moves = 0
        self.solved = False

    def generate_puzzle(self):
        numbers = list(range(1, self.puzzle_size ** 2))
        random.shuffle(numbers)
        numbers.append(0)  # 0 represents the empty tile
        return [numbers[i:i+self.puzzle_size] for i in range(0, len(numbers), self.puzzle_size)]

    def draw(self):
        self.screen.fill((255, 255, 255))
        for y in range(self.puzzle_size):
            for x in range(self.puzzle_size):
                if self.puzzle[y][x] != 0:
                    pygame.draw.rect(self.screen, (0, 0, 0), (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size), 2)
                    text = self.font.render(str(self.puzzle[y][x]), True, (0, 0, 0))
                    text_rect = text.get_rect(center=((x + 0.5) * self.tile_size, (y + 0.5) * self.tile_size))
                    self.screen.blit(text, text_rect)
        
        moves_text = self.font.render(f"Moves: {self.moves}", True, (0, 0, 0))
        self.screen.blit(moves_text, (10, self.puzzle_size * self.tile_size + 10))

        if self.solved:
            solved_text = self.font.render("Puzzle Solved!", True, (0, 255, 0))
            self.screen.blit(solved_text, (10, self.puzzle_size * self.tile_size + 50))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.solved:
            x, y = event.pos
            tile_x, tile_y = x // self.tile_size, y // self.tile_size
            if self.is_valid_move(tile_x, tile_y):
                self.swap_tiles(tile_x, tile_y)
                self.moves += 1
                self.solved = self.check_solved()
                if self.solved:
                    return True
        return False

    def is_valid_move(self, x, y):
        return (abs(x - self.empty_tile[0]) + abs(y - self.empty_tile[1])) == 1

    def swap_tiles(self, x, y):
        self.puzzle[y][x], self.puzzle[self.empty_tile[1]][self.empty_tile[0]] = self.puzzle[self.empty_tile[1]][self.empty_tile[0]], self.puzzle[y][x]
        self.empty_tile = (x, y)

    def check_solved(self):
        flat_puzzle = [item for sublist in self.puzzle for item in sublist]
        return flat_puzzle == list(range(1, self.puzzle_size ** 2)) + [0]

    def update(self, dt):
        pass

    def render(self, screen):
        self.draw()

    def get_score(self):
        return 100 if self.solved else 0