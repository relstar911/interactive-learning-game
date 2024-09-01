import pygame
from asset_manager import AssetManager

class Character(pygame.sprite.Sprite):
    def __init__(self, asset_manager):
        super().__init__()
        self.image = asset_manager.get_sprite('character')
        self.rect = self.image.get_rect()

class NPC(pygame.sprite.Sprite):
    def __init__(self, asset_manager, npc_type):
        super().__init__()
        self.image = asset_manager.get_sprite(f'npc{npc_type}')
        self.rect = self.image.get_rect()

# ... andere Sprite-Klassen ...