import pygame
from logger import logger
from content.asset_config import SPRITE_MAPPINGS

class NPC(pygame.sprite.Sprite):
    def __init__(self, npc_data, asset_manager):
        super().__init__()
        self.name = npc_data["name"]
        self.role = npc_data["role"]
        self.position = npc_data["position"]
        self.dialogue = npc_data["dialogue"]
        self.sprite_sheet = asset_manager.get_sprite('npc')
        self.image = self.get_image(0, 0, 32, 32)  # Assuming 32x32 grid for slime
        self.rect = self.image.get_rect(topleft=self.position)
        self.animation_index = 0

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image

    def update(self, dt):
        self.animation_index = (self.animation_index + 1) % 3
        self.image = self.get_image(self.animation_index * 32, 0, 32, 32)

    def draw(self, surface, camera):
        surface.blit(self.image, camera.apply(self))

    def interact(self, game_tasks):
        logger.info(f"{self.name} is interacting.")
        return self.dialogue.get("greeting", f"Hello, I'm {self.name}!")

    def get_dialogue_options(self):
        return self.dialogue.get("options", [])