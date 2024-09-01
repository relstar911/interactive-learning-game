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
        self.player_speed = 5  # oder einen anderen geeigneten Wert
        
        # Asset-Pfade
        self.asset_dir = "assets"
        self.font_dir = os.path.join(self.asset_dir, "fonts")
        self.sound_dir = os.path.join(self.asset_dir, "sounds")
        self.sprite_dir = os.path.join(self.asset_dir, "sprites")
        
        # Spieler-Konfiguration
        self.max_player_name_length = 15
        self.initial_player_level = 1
        self.xp_per_level = 100

        # Neue Konfigurationen aus config.json
        self.asset_paths = {
            "sprites": {
                "texture": os.path.join(self.asset_dir, "sprites", "Texture"),
                "prototype": os.path.join(self.asset_dir, "sprites", "prototype"),
                "buildings": os.path.join(self.asset_dir, "sprites", "buildings")
            },
            "fonts": os.path.join(self.asset_dir, "fonts", "Raleway"),
            "sounds": os.path.join(self.asset_dir, "sounds"),
            "music": os.path.join(self.asset_dir, "music")
        }

        self.sprite_files = {
            "player": "TX Player.png",
            "tutor": "TX Props.png",
            "quizmaster": "TX Props.png",
            "gamemaster": "TX Props.png",
            "book": "TX Props.png",
            "potion": "TX Props.png",
            "scroll": "TX Props.png",
            "coin": "TX Props.png",
            "background": "TX Tileset Grass.png",
            "tree": "TX Plant.png",
            "npc1": "TX Player.png",
            "npc2": "TX Player.png",
            "npc3": "TX Player.png"
        }

        self.prototype_sprites = {
            "tilesheet": "tilesheet.png",
            "tilesheet_complete": "tilesheet_complete.png",
            "character": "character.png"
        }

        self.building_sprites = {
            "tilesheet": "tilesheet.png",
            "tilesheet_complete": "tilesheet_complete.png"
        }

        self.font_files = {
            "main": "Raleway-Regular.ttf",
            "bold": "Raleway-Bold.ttf",
            "italic": "Raleway-Italic.ttf"
        }

        self.sound_files = {
            "pickup": "pickup.wav",
            "interact": "interact.wav",
            "levelup": "levelup.wav"
        }

        self.music_files = {
            "background": "background_music.mp3"
        }

        self.log_level = 'DEBUG'  # Sie können dies auf 'INFO', 'WARNING', etc. ändern

    def get(self, key, default=None):
        return getattr(self, key, default)

config = Config()