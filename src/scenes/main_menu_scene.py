import pygame
from scenes.base_scene import BaseScene
from game_states import GameState
from logger import logger

class MainMenuScene(BaseScene):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = self.game_engine.asset_manager.get_font('raleway', 48, 'bold')
        self.menu_items = ["Start Game", "Options", "Quit"]
        self.selected_item = 0
        logger.info("MainMenuScene initialized")

    def enter(self):
        logger.info("Entering MainMenuScene")
        self.game_engine.play_start_music()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_item = (self.selected_item - 1) % len(self.menu_items)
                logger.debug(f"Selected item: {self.menu_items[self.selected_item]}")
            elif event.key == pygame.K_DOWN:
                self.selected_item = (self.selected_item + 1) % len(self.menu_items)
                logger.debug(f"Selected item: {self.menu_items[self.selected_item]}")
            elif event.key == pygame.K_RETURN:
                self.select_menu_item()

    def select_menu_item(self):
        logger.info(f"Selected menu item: {self.menu_items[self.selected_item]}")
        if self.menu_items[self.selected_item] == "Start Game":
            self.game_engine.scene_manager.set_scene(GameState.CHARACTER_CREATION)
        elif self.menu_items[self.selected_item] == "Options":
            # Implement options menu
            pass
        elif self.menu_items[self.selected_item] == "Quit":
            logger.info("Quitting game from main menu")
            self.game_engine.running = False

    def update(self, dt):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        for i, item in enumerate(self.menu_items):
            color = (255, 255, 255) if i == self.selected_item else (128, 128, 128)
            text = self.font.render(item, True, color)
            text_rect = text.get_rect(center=(self.game_engine.width // 2, 200 + i * 100))
            screen.blit(text, text_rect)