import pygame
import sys
from game_engine import game_engine
from scenes.main_menu import MainMenuScene
from logger import logger

def main():
    try:
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
