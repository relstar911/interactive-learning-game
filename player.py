import pygame
from inventory import Inventory
from config import config
from logger import logger
from content.game_content import CHARACTERS, ONBOARDING_PROGRESS
from content.asset_config import SPRITE_MAPPINGS

class Player(pygame.sprite.Sprite):
    def __init__(self, name, asset_manager):
        super().__init__()
        player_data = CHARACTERS["player"]
        self.name = name
        self.xp = 0
        self.level = player_data["initial_level"]
        self.sprite_sheet = asset_manager.get_sprite('player')
        self.image = self.get_image(0, 0, 48, 48)  # Assuming 48x48 grid
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = player_data["initial_position"]
        self.inventory = Inventory()
        self.speed = player_data["speed"]
        self.score = 0
        self.onboarding_progress = {category: 0 for category in ONBOARDING_PROGRESS}
        self.animation_index = 0
        self.facing_right = True

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.update_animation()
        logger.debug(f"Player '{self.name}' moved to ({self.rect.x}, {self.rect.y})")

    def update_animation(self):
        self.animation_index = (self.animation_index + 1) % 3
        row = 3 if (self.rect.x != 0 or self.rect.y != 0) else 0
        col = self.animation_index
        self.image = self.get_image(col * 48, row * 48, 48, 48)
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        if dx != 0 or dy != 0:
            self.move(dx, dy)
        if dx > 0:
            self.facing_right = True
        elif dx < 0:
            self.facing_right = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)

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

    def update_onboarding_progress(self, category, points):
        if category in self.onboarding_progress:
            self.onboarding_progress[category] = min(self.onboarding_progress[category] + points, ONBOARDING_PROGRESS[category]['max_score'])
            logger.info(f"Updated {category} progress: {self.onboarding_progress[category]}/{ONBOARDING_PROGRESS[category]['max_score']}")