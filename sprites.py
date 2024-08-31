import pygame
from asset_manager import asset_manager

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = asset_manager.get_sprite('player')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class NPCSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_name):
        super().__init__()
        self.image = asset_manager.get_sprite(sprite_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y