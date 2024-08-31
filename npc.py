import pygame
from asset_manager import asset_manager
from llm_integration import generate_response

class NPC(pygame.sprite.Sprite):
    def __init__(self, name, x, y, role, sprite_name):
        super().__init__()
        self.name = name
        self.role = role
        self.sprites = asset_manager.get_sprite(sprite_name)
        self.image = self.sprites[0] if isinstance(self.sprites, list) else self.sprites
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dialogue_history = []
        self.animation_index = 0
        self.animation_timer = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def interact(self, player_input):
        context = "\n".join(self.dialogue_history[-5:])  # Last 5 interactions as context
        prompt = f"Du bist ein {self.role} in einem Lernspiel. Bisheriger Kontext:\n{context}\nDer Spieler sagt: '{player_input}'. Antworte kurz und hilfreich:"
        response = generate_response(prompt)
        self.dialogue_history.append(f"Spieler: {player_input}")
        self.dialogue_history.append(f"{self.name}: {response}")
        return response

    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer > 200:  # Change frame every 200 ms
            self.animation_timer = 0
            self.animation_index = (self.animation_index + 1) % len(self.sprites)
            self.image = self.sprites[self.animation_index]