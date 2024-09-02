import pygame
from content.game_content import NPC_DIALOGUES
from config import config

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, name, role, asset_manager):
        super().__init__()
        self.name = name
        self.role = role
        self.position = (x, y)
        self.dialogue = NPC_DIALOGUES.get(self.role, {
            "greeting": f"Hello, I'm {self.name}.",
            "options": [
                {"text": "Goodbye", "response": "Farewell!"}
            ]
        })
        
        self.sprite = asset_manager.get_sprite(f"{role.lower()}_sprite")
        if self.sprite:
            self.image = self.sprite
            self.rect = self.image.get_rect(topleft=self.position)
        else:
            self.image = pygame.Surface((40, 40))
            self.image.fill((255, 0, 0))  # Red square as fallback
            self.rect = self.image.get_rect(topleft=self.position)

    def update(self, dt):
        # Here we can add animations or movements later
        pass

    def render(self, screen, camera=None):
        if camera:
            screen.blit(self.image, camera.apply(self))
        else:
            screen.blit(self.image, self.rect)
        
        font = pygame.font.Font(None, 20)
        text = font.render(self.role, True, (255, 255, 255))
        text_rect = text.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 5)
        screen.blit(text, text_rect)

    def get_dialogue(self):
        print(f"Dialogue for {self.name}: {self.dialogue}")  # Debug print
        return self.dialogue

    def interact(self):
        return self.get_dialogue()