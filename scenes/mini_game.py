import pygame
from scenes.base_scene import BaseScene
from mini_game import MemoryGame

class MiniGameScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.mini_game = MemoryGame(game_engine.screen, pygame.font.Font(None, 36))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            from scenes.game_world import GameWorldScene
            self.game_engine.change_scene(GameWorldScene(self.game_engine))
        else:
            game_over = self.mini_game.handle_event(event)
            if game_over:
                self.game_engine.player.gain_xp(self.mini_game.get_score() * 5)
                from scenes.game_world import GameWorldScene
                self.game_engine.change_scene(GameWorldScene(self.game_engine))

    def update(self, dt):
        self.mini_game.update(dt)

    def render(self, screen):
        self.mini_game.draw()
        # Hinzufügen eines Hinweises zum Schließen des Mini-Spiels
        font = pygame.font.Font(None, 24)
        text = font.render("Drücke M, um zum Hauptspiel zurückzukehren", True, (255, 255, 255))
        screen.blit(text, (10, screen.get_height() - 30))