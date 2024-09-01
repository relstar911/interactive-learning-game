import os
import pygame
import sys
from game_engine import game_engine
from scenes.main_menu import MainMenuScene
from logger import logger
from constants import SPRITES_DIR, SOUNDS_DIR, FONTS_DIR

def check_directories():
    for directory in [SPRITES_DIR, SOUNDS_DIR, FONTS_DIR]:
        if not os.path.exists(directory):
            logger.warning(f"Directory does not exist: {directory}")
        else:
            logger.info(f"Directory exists: {directory}")
            print(f"Contents of {directory}:")
            for file in os.listdir(directory):
                print(f"  - {file}")

def main():
    try:
        check_directories()
        logger.info("Starting the game")
        pygame.init()
        logger.info("Pygame initialized")
        main_menu = MainMenuScene(game_engine)
        logger.info("Main menu scene created")
        game_engine.change_scene(main_menu)
        logger.info("Changed to main menu scene")
        game_engine.run()
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
    finally:
        logger.info("Game closing")
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
