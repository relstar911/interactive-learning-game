import os
import pygame
from config import config

class AssetManager:
    def __init__(self):
        self.assets = {
            'fonts': {},
            'sounds': {},
            'sprites': {},
            'models': {}
        }
        self.load_assets()

    def load_assets(self):
        self.load_fonts()
        self.load_sounds()
        self.load_sprites()

    def load_fonts(self):
        font_path = os.path.join(config.font_dir, 'Raleway', 'Raleway-4.101', 'static', 'TTF')
        font_sizes = [24, 32, 48]  # Verschiedene Größen für unterschiedliche Zwecke
        for size in font_sizes:
            self.assets['fonts'][f'raleway_{size}'] = {
                'regular': pygame.font.Font(os.path.join(font_path, 'Raleway-Regular.ttf'), size),
                'bold': pygame.font.Font(os.path.join(font_path, 'Raleway-Bold.ttf'), size)
            }

    def load_sounds(self):
        sound_files = {
            'telecom': '1350180_TeleCom-INC.mp3',
            'backshots': '1352396_I-Gave-Them-Backshots.mp3',
            'piano': '1354018_288-Autograph-Piano-2023.mp3',
            'island': '1354837_Timeless-Island-Surreal-x-.mp3'
        }
        for name, file in sound_files.items():
            sound_path = os.path.join(config.sound_dir, file)
            if os.path.exists(sound_path):
                self.assets['sounds'][name] = sound_path  # Speichern Sie den Pfad anstelle des Sound-Objekts
            else:
                print(f"Warnung: Sounddatei '{file}' nicht gefunden.")

    def load_sprites(self):
        sprite_files = [
            'character.png', 'npc1.png', 'npc2.png', 'npc3.png',
            'book.png', 'potion.png', 'tilemap.png'
        ]
        for file in sprite_files:
            name = os.path.splitext(file)[0]
            self.assets['sprites'][name] = pygame.image.load(os.path.join(config.sprite_dir, file)).convert_alpha()

    def get_font(self, name, size=24, style='regular'):
        return self.assets['fonts'].get(f'{name}_{size}', {}).get(style)

    def get_sound(self, name):
        return self.assets['sounds'].get(name)

    def get_sprite(self, name):
        return self.assets['sprites'].get(name)

    def get_model(self, name):
        return self.assets['models'].get(name)

# Wir erstellen die Instanz nicht hier, sondern in der game_engine.py