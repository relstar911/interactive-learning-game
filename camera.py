import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(self.width / 2)
        y = -target.rect.y + int(self.height / 2)

        # Limit scrolling to game map
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.camera.width - self.width), x)  # right
        y = max(-(self.camera.height - self.height), y)  # bottom

        self.camera = pygame.Rect(x, y, self.width, self.height)