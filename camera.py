import pygame
from logger import logger

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return pygame.Rect(entity.rect.x - self.camera.x, entity.rect.y - self.camera.y, entity.rect.width, entity.rect.height)

    def apply_rect(self, rect):
        return pygame.Rect(rect.x - self.camera.x, rect.y - self.camera.y, rect.width, rect.height)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)
        
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - self.camera.width), x)
        y = max(-(self.height - self.camera.height), y)
        
        self.camera = pygame.Rect(x, y, self.width, self.height)
        logger.debug(f"Camera updated: ({self.camera.x}, {self.camera.y})")