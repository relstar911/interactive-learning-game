import pygame
import sys
from game_engine import game_engine
from scenes.main_menu import MainMenuScene

def main():
    try:
        pygame.init()
        main_menu = MainMenuScene(game_engine)
        game_engine.change_scene(main_menu)
        game_engine.run()
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
