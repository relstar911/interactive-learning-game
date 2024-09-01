import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        if not self.openai_api_key:
            print("Warning: OPENAI_API_KEY not found in environment variables. Some features may not work.")
        
        # Spielfenster-Konfiguration
        self.window_width = 800
        self.window_height = 600
        self.window_title = "Interactive Learning Game"
        
        # Spiel-Konfiguration
        self.fps = 60
        self.player_speed = 5
        
        # Asset-Pfade
        self.asset_dir = "assets"
        self.font_dir = os.path.join(self.asset_dir, "fonts")
        self.sound_dir = os.path.join(self.asset_dir, "sounds")
        self.sprite_dir = os.path.join(self.asset_dir, "sprites")
        
        # Spieler-Konfiguration
        self.max_player_name_length = 15
        self.initial_player_level = 1
        self.xp_per_level = 100

    def get(self, key, default=None):
        return getattr(self, key, default)

config = Config()