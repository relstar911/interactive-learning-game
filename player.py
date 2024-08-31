import pygame
from inventory import Inventory
from asset_manager import asset_manager

class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.xp = 0
        self.level = 1
        self.sprites = asset_manager.get_sprite('player')
        if isinstance(self.sprites, list):
            self.current_frame = 0
            self.image = self.sprites[self.current_frame]
        else:
            self.image = self.sprites  # Wenn es nur ein einzelnes Surface ist
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.inventory = Inventory()
        self.tutorial_completed = False
        self.quiz_correct_answers = 0
        self.memory_game_won = False
        self.speed = 3
        self.animation_timer = 0
        self.animation_speed = 200  # Milliseconds per frame

    def move(self, dx, dy):
        new_x = self.rect.x + dx * self.speed
        new_y = self.rect.y + dy * self.speed
        
        # Simple collision detection with screen edges
        if 0 <= new_x <= 800 - self.rect.width:
            self.rect.x = new_x
        if 0 <= new_y <= 600 - self.rect.height:
            self.rect.y = new_y

        # Update animation when player moves
        if dx != 0 or dy != 0:
            self.update_animation()

    def update_animation(self):
        if isinstance(self.sprites, list):
            self.animation_timer += 16  # Assuming 60 FPS, so about 16ms per frame
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.current_frame = (self.current_frame + 1) % len(self.sprites)
                self.image = self.sprites[self.current_frame]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.level * 100:
            self.level_up()

    def check_level_up(self):
        if self.xp >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= (self.level - 1) * 100
        print(f"{self.name} has leveled up to level {self.level}!")
        # Hier könnten Sie Belohnungen für das Leveln hinzufügen, z.B.:
        # self.max_health += 10
        # self.attack_power += 2

    def add_to_inventory(self, item):
        self.inventory.add_item(item)

    def remove_from_inventory(self, item):
        self.inventory.remove_item(item)

    def get_inventory(self):
        return self.inventory.get_items()

    def complete_tutorial(self):
        self.tutorial_completed = True

    def answer_quiz_correctly(self):
        self.quiz_correct_answers += 1

    def win_memory_game(self):
        self.memory_game_won = True