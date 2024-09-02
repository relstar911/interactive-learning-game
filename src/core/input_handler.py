import pygame

class InputHandler:
    def __init__(self):
        self.keys_pressed = set()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.keys_pressed.add(event.key)
        elif event.type == pygame.KEYUP:
            self.keys_pressed.discard(event.key)

    def is_key_pressed(self, key):
        return key in self.keys_pressed
