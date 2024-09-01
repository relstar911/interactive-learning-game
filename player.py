import pygame
from inventory import Inventory
from config import config

class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y, asset_manager):
        super().__init__()
        self.name = name
        self.xp = 0
        self.level = config.get('initial_player_level')
        self.sprite = asset_manager.get_sprite('character')
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.inventory = Inventory()
        self.speed = config.get('player_speed')
        self.score = 0

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        print(f"Player position updated: ({self.rect.x}, {self.rect.y})")  # Debugging-Ausgabe

    def update_score(self, correct):
        if correct:
            self.score += 10
            self.gain_xp(20)
        else:
            self.score -= 5

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.level * config.get('xp_per_level'):
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= (self.level - 1) * config.get('xp_per_level')
        print(f"{self.name} has leveled up to level {self.level}!")

    def add_to_inventory(self, item):
        self.inventory.add_item(item)

    def get_inventory(self):
        return self.inventory.get_items()

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
        print(f"Player position set to: ({self.rect.x}, {self.rect.y})")