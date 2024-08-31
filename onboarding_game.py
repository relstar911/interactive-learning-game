import pygame
from game_engine import game_engine
from scenes.main_menu import MainMenuScene
from asset_manager import asset_manager
from logger import logger
from config import config

def main():
    pygame.init()
    asset_manager.load_all_assets()
    logger.info("Starting game")
    
    if not config.get('openai_api_key'):
        print("Warning: OpenAI API key is not set. Some features may not work.")
    
    # Überprüfen Sie, ob alle erforderlichen Assets geladen wurden
    missing_assets = [name for name, asset in asset_manager.sprites.items() if asset is None]
    missing_assets.extend([name for name, asset in asset_manager.fonts.items() if asset is None])
    missing_assets.extend([name for name, asset in asset_manager.sounds.items() if asset is None])
    missing_assets.extend([name for name, asset in asset_manager.music.items() if asset is None])
    
    if missing_assets:
        print(f"Warning: The following assets could not be loaded: {', '.join(missing_assets)}")
    
    main_menu = MainMenuScene(game_engine)
    game_engine.change_scene(main_menu)
    
    game_engine.run()

if __name__ == "__main__":
    main()
