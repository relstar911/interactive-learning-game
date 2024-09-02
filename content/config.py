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
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.sprite_dir = os.path.join(self.base_dir, "sprites")
        self.character_dir = os.path.join(self.sprite_dir, "characters")
        self.asset_dir = os.path.join(self.sprite_dir, "assets")
        self.font_dir = os.path.join(self.asset_dir, "fonts")
        self.sound_dir = os.path.join(self.asset_dir, "sounds")
        self.texture_dir = os.path.join(self.asset_dir, "sprites", "Texture")
        
        # Spieler-Konfiguration
        self.max_player_name_length = 15
        self.initial_player_level = 1
        self.xp_per_level = 100

        # Asset-Pfade aus config.json
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

        # Sprite-Dateien
        self.sprite_files = {
            "player": os.path.join(self.character_dir, "player.png"),
            "npc": os.path.join(self.character_dir, "slime.png"),
            "tilemap": os.path.join(self.texture_dir, "TX Tileset Grass.png"),
            "tutor": os.path.join(self.texture_dir, "TX Props.png"),
            "quizmaster": os.path.join(self.texture_dir, "TX Props.png"),
            "gamemaster": os.path.join(self.texture_dir, "TX Props.png"),
            "book": os.path.join(self.texture_dir, "TX Props.png"),
            "potion": os.path.join(self.texture_dir, "TX Props.png"),
            "scroll": os.path.join(self.texture_dir, "TX Props.png"),
            "coin": os.path.join(self.texture_dir, "TX Props.png"),
            "background": os.path.join(self.texture_dir, "TX Tileset Grass.png"),
            "tree": os.path.join(self.texture_dir, "TX Plant.png"),
            "chest": os.path.join(self.texture_dir, "TX Props.png"),
            "npc_hr_manager": os.path.join(self.character_dir, "hr_manager.png"),
            "npc_it_specialist": os.path.join(self.character_dir, "it_specialist.png"),
            "npc_team_lead": os.path.join(self.character_dir, "team_lead.png"),
            "npc_coworker": os.path.join(self.character_dir, "coworker.png"),
            "kiosk": os.path.join(self.texture_dir, "kiosk.png"),
            "terminal": os.path.join(self.texture_dir, "terminal.png"),
            "meeting_room": os.path.join(self.texture_dir, "meeting_room.png")
        }

        # Prototyp-Sprites
        self.prototype_sprites = {
            "tilesheet": "tilesheet.png",
            "tilesheet_complete": "tilesheet_complete.png",
            "character": "character.png"
        }

        # Gebäude-Sprites
        self.building_sprites = {
            "tilesheet": "tilesheet.png",
            "tilesheet_complete": "tilesheet_complete.png"
        }

        # Schriftarten
        self.font_files = {
            "regular": os.path.join(self.font_dir, "Raleway", "Raleway-4.101", "variable", "TTF", "Raleway-VF.ttf"),
            "italic": os.path.join(self.font_dir, "Raleway", "Raleway-4.101", "variable", "TTF", "Raleway-Italic-VF.ttf"),
            "bold": os.path.join(self.font_dir, "Raleway", "Raleway-4.101", "variable", "TTF", "Raleway-VF.ttf")  # Hinzugefügt
        }

        # Soundeffekte und Musik
        self.sound_files = {
            "menu_music": os.path.join(self.sound_dir, "1354018_288-Autograph-Piano-2023.mp3"),
            "game_music": os.path.join(self.sound_dir, "1350180_TeleCom-INC.mp3")
        }

        # Musik
        self.music_files = {
            "background": "background_music.mp3"
        }

        # Logging-Konfiguration
        self.log_level = 'DEBUG'

        # Minispiel-Konfigurationen
        self.memory_game_size = 4
        self.company_bingo_size = 4

        # XP-Belohnungen
        self.xp_per_quiz_correct = 10
        self.xp_per_minigame_win = 50

    def get(self, key, default=None):
        return getattr(self, key, default)

config = Config()