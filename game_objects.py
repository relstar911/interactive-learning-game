import pygame
from logger import logger
from content.asset_config import SPRITE_MAPPINGS

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, name, description, asset_manager, sprite_name):
        super().__init__()
        self.name = name
        self.description = description
        self.sprite_sheet = asset_manager.get_sprite(sprite_name)
        self.image = self.get_image(0, 0, 32, 32)  # Assuming 32x32 for objects
        self.rect = self.image.get_rect(topleft=(x, y))

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image

    def interact(self):
        return self.description

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self))