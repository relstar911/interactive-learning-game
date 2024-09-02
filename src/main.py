import os
import pygame
import sys
from src.core.game_engine import GameEngine
from src.scenes.main_menu_scene import MainMenuScene
from src.scenes.world_scene import WorldScene
from src.utils.logger import setup_logger, logger
from content.config import config

def check_directories():
    directories = [config.sprite_dir, config.sound_dir, config.font_dir]
    for directory in directories:
        if not os.path.exists(directory):
            logger.warning(f"Directory does not exist: {directory}")
        else:
            logger.info(f"Directory exists: {directory}")
            logger.debug(f"Contents of {directory}:")
            for file in os.listdir(directory):
                logger.debug(f"  - {file}")

def main():
    setup_logger()
    try:
        check_directories()
        logger.info("Starting the game")
        pygame.init()
        logger.info("Pygame initialized")
        
        screen = pygame.display.set_mode((config.window_width, config.window_height))
        pygame.display.set_caption(config.window_title)
        
        game_engine = GameEngine(screen)
        main_menu = MainMenuScene(game_engine)
        world_scene = WorldScene(game_engine)
        
        game_engine.scene_manager.add_scene("main_menu", main_menu)
        game_engine.scene_manager.add_scene("world", world_scene)
        game_engine.scene_manager.set_scene("main_menu")
        
        logger.info("Scenes created and set")
        
        game_engine.run()
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
    finally:
        logger.info("Game closing")
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
