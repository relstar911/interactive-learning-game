import pygame
from inventory import Item
from asset_manager import asset_manager

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_name, name, description):
        super().__init__()
        self.sprite_name = sprite_name
        self.image = asset_manager.get_sprite(sprite_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.item = Item(name, description)

    def interact(self, player):
        player.add_to_inventory(self.item)
        return f"Du hast {self.item.name} aufgehoben. {self.item.description}"

    def draw(self, screen):
        screen.blit(self.image, self.rect)