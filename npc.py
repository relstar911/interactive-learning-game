import pygame
from config import config

class NPC:
    def __init__(self, name, position, dialogue, sprite_name="default_npc"):
        self.name = name
        self.position = position
        self.dialogue = dialogue
        self.sprite_name = sprite_name
        self.sprite = None
        self.rect = pygame.Rect(position[0], position[1], 50, 50)  # Platzhalter-Größe

    def load_sprite(self, asset_manager):
        self.sprite = asset_manager.get_sprite(self.sprite_name)
        if self.sprite is None:
            print(f"Warnung: Sprite '{self.sprite_name}' für NPC '{self.name}' nicht gefunden.")
        else:
            self.rect = self.sprite.get_rect(topleft=self.position)

    def draw(self, surface):
        if self.sprite:
            surface.blit(self.sprite, self.rect)
        else:
            pygame.draw.rect(surface, (0, 255, 0), self.rect)  # Grünes Rechteck als Platzhalter

    def get_questions(self):
        # Hier würden Sie Fragen basierend auf dem NPC-Typ zurückgeben
        return [
            {
                "question": f"What is the role of {self.name}?",
                "options": ["Manager", "Developer", "Designer", "HR Specialist"],
                "correct": 0
            },
            {
                "question": "What's our company's main value?",
                "options": ["Money", "Innovation", "People", "Technology"],
                "correct": 2
            },
        ]

# Die DialogueTree und DialogueNode Klassen können Sie später implementieren, wenn Sie das Dialogsystem erweitern.