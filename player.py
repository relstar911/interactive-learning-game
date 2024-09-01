import pygame
from inventory import Inventory
from config import config
from logger import logger

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
        logger.info(f"Player '{name}' created at position ({x}, {y})")

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        logger.debug(f"Player '{self.name}' moved to ({self.rect.x}, {self.rect.y})")

    def update_score(self, correct):
        if correct:
            self.score += 10
            self.gain_xp(20)
            logger.info(f"Player '{self.name}' answered correctly. New score: {self.score}")
        else:
            self.score -= 5
            logger.info(f"Player '{self.name}' answered incorrectly. New score: {self.score}")

    def gain_xp(self, amount):
        self.xp += amount
        logger.info(f"Player '{self.name}' gained {amount} XP. Total XP: {self.xp}")
        while self.xp >= self.level * config.get('xp_per_level'):
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= (self.level - 1) * config.get('xp_per_level')
        logger.info(f"Player '{self.name}' leveled up to level {self.level}!")

    def add_to_inventory(self, item):
        self.inventory.add_item(item)
        logger.info(f"Player '{self.name}' added '{item.name}' to inventory")

    def get_inventory(self):
        return self.inventory.get_items()

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
        logger.debug(f"Player '{self.name}' position set to ({self.rect.x}, {self.rect.y})")