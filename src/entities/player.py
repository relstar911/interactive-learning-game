import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.walk_speed = 3
        self.run_speed = 6
        self.color = (0, 0, 255)  # Blue color for the player
        self.velocity = [0, 0]
        self.running = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                self.running = True
            self.update_velocity(event.key, True)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                self.running = False
            self.update_velocity(event.key, False)

    def update_velocity(self, key, pressed):
        speed = self.run_speed if self.running else self.walk_speed
        if key == pygame.K_LEFT:
            self.velocity[0] = -speed if pressed else 0
        elif key == pygame.K_RIGHT:
            self.velocity[0] = speed if pressed else 0
        elif key == pygame.K_UP:
            self.velocity[1] = -speed if pressed else 0
        elif key == pygame.K_DOWN:
            self.velocity[1] = speed if pressed else 0

    def update(self, dt):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
