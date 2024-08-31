import pygame
import os
from config import config

class AssetManager:
    def __init__(self):
        self.sprites = {}
        self.prototype_sprites = {}
        self.building_sprites = {}
        self.fonts = {}
        self.sounds = {}
        self.music = {}

    def load_all_assets(self):
        self.load_all_sprites()
        self.load_all_prototype_sprites()
        self.load_all_building_sprites()
        self.load_all_fonts()
        self.load_all_sounds()
        self.load_all_music()

    def load_all_sprites(self):
        sprite_config = config.get('sprites', {})
        for sprite_name, filename in sprite_config.items():
            self.load_sprite(sprite_name, filename, 'texture')

    def load_all_prototype_sprites(self):
        prototype_config = config.get('prototype_sprites', {})
        for sprite_name, filename in prototype_config.items():
            self.load_sprite(sprite_name, filename, 'prototype', self.prototype_sprites)

    def load_all_building_sprites(self):
        building_config = config.get('building_sprites', {})
        for sprite_name, filename in building_config.items():
            self.load_sprite(sprite_name, filename, 'buildings', self.building_sprites)

    def load_sprite(self, name, filename, category, target_dict=None):
        if target_dict is None:
            target_dict = self.sprites
        fullpath = os.path.join(config.get(f'assets.sprites.{category}', f'assets/sprites/{category}/'), filename)
        print(f"Attempting to load sprite: {name} from {fullpath}")
        if os.path.exists(fullpath):
            try:
                sprite_sheet = pygame.image.load(fullpath).convert_alpha()
                if name == 'background':
                    window_size = (config.get('window.width', 800), config.get('window.height', 600))
                    target_dict[name] = pygame.transform.scale(sprite_sheet, window_size)
                elif name in ['book', 'potion', 'scroll', 'coin']:
                    target_dict[name] = self.extract_sprite(sprite_sheet, 0, 0, 32, 32)
                elif name.startswith('npc') or name == 'player' or name == 'tree':
                    target_dict[name] = [
                        self.extract_sprite(sprite_sheet, 0, 0, 32, 32),
                        self.extract_sprite(sprite_sheet, 32, 0, 32, 32),
                        self.extract_sprite(sprite_sheet, 64, 0, 32, 32)
                    ]
                else:
                    target_dict[name] = sprite_sheet
                print(f"Successfully loaded sprite: {name}")
            except pygame.error as e:
                print(f"Error loading sprite {name}: {e}")
                target_dict[name] = self.create_placeholder_image(50, 50, self.get_color_for_sprite(name))
        else:
            print(f"Sprite file '{fullpath}' not found. Using placeholder.")
            target_dict[name] = self.create_placeholder_image(50, 50, self.get_color_for_sprite(name))

    def load_all_fonts(self):
        font_config = config.get('fonts', {})
        for font_name, filename in font_config.items():
            self.load_font(font_name, filename)

    def load_font(self, name, filename, size=36):
        fullpath = os.path.join(config.get('assets.fonts', 'assets/fonts/Raleway/'), filename)
        print(f"Attempting to load font: {name} from {fullpath}")
        if os.path.exists(fullpath):
            try:
                self.fonts[name] = pygame.font.Font(fullpath, size)
                print(f"Successfully loaded font: {name}")
            except pygame.error as e:
                print(f"Error loading font {name}: {e}")
                self.fonts[name] = pygame.font.Font(None, size)
        else:
            print(f"Font file '{fullpath}' not found. Using default font.")
            self.fonts[name] = pygame.font.Font(None, size)

    def load_all_sounds(self):
        sound_config = config.get('sounds', {})
        for sound_name, filename in sound_config.items():
            self.load_sound(sound_name, filename)

    def load_sound(self, name, filename):
        fullpath = os.path.join(config.get('assets.sounds', 'assets/sounds/'), filename)
        print(f"Attempting to load sound: {name} from {fullpath}")
        if os.path.exists(fullpath):
            try:
                self.sounds[name] = pygame.mixer.Sound(fullpath)
                print(f"Successfully loaded sound: {name}")
            except pygame.error as e:
                print(f"Error loading sound {name}: {e}")
        else:
            print(f"Sound file '{fullpath}' not found. Using silent placeholder.")
            self.sounds[name] = pygame.mixer.Sound(buffer=b'\x00' * 44100)  # 1 second of silence

    def load_all_music(self):
        music_config = config.get('music', {})
        for music_name, filename in music_config.items():
            self.load_music(music_name, filename)

    def load_music(self, name, filename):
        fullpath = os.path.join(config.get('assets.music', 'assets/music/'), filename)
        print(f"Attempting to load music: {name} from {fullpath}")
        if os.path.exists(fullpath):
            self.music[name] = fullpath
            print(f"Successfully loaded music: {name}")
        else:
            print(f"Music file '{fullpath}' not found. Music will be silent.")
            self.music[name] = None

    def extract_sprite(self, sheet, x, y, width, height):
        """Extrahiert einen einzelnen Sprite aus einem Spritesheet."""
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(sheet, (0, 0), (x, y, width, height))
        return sprite

    def get_sprite(self, name, category='texture'):
        if category == 'prototype':
            return self.prototype_sprites.get(name, self.create_placeholder_image(50, 50, self.get_color_for_sprite(name)))
        elif category == 'buildings':
            return self.building_sprites.get(name, self.create_placeholder_image(50, 50, self.get_color_for_sprite(name)))
        else:
            return self.sprites.get(name, self.create_placeholder_image(50, 50, self.get_color_for_sprite(name)))

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()
        else:
            print(f"Sound '{name}' not found. Playing nothing.")

    def play_music(self, name):
        if name in self.music and self.music[name]:
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(-1)  # -1 means loop indefinitely
        else:
            print(f"Music '{name}' not found or is None. Playing nothing.")

    @staticmethod
    def create_placeholder_image(width, height, color):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.fill(color)
        return image

    @staticmethod
    def get_color_for_sprite(name):
        colors = {
            'player': (0, 255, 0, 128),  # Semi-transparent Green
            'tutor': (255, 0, 0, 128),   # Semi-transparent Red
            'quizmaster': (0, 0, 255, 128),  # Semi-transparent Blue
            'gamemaster': (255, 255, 0, 128),  # Semi-transparent Yellow
            'book': (128, 0, 128, 128),  # Semi-transparent Purple
            'potion': (0, 255, 255, 128),  # Semi-transparent Cyan
            'background': (100, 100, 100, 255),  # Opaque Gray
            'npc1': (255, 128, 0, 128),  # Semi-transparent Orange
            'npc2': (0, 128, 255, 128),  # Semi-transparent Light Blue
            'npc3': (128, 255, 0, 128),  # Semi-transparent Lime
            'scroll': (255, 255, 128, 128),  # Semi-transparent Light Yellow
            'coin': (255, 215, 0, 128),  # Semi-transparent Gold
            'tree': (0, 100, 0, 128)  # Semi-transparent Dark Green
        }
        return colors.get(name, (200, 200, 200, 128))  # Semi-transparent light gray if name not found

    def get_font(self, name, size=36):
        if name not in self.fonts:
            print(f"Font '{name}' not loaded. Using default font.")
            return pygame.font.Font(None, size)
        return self.fonts[name]

asset_manager = AssetManager()

print("Loading all assets...")
asset_manager.load_all_assets()
print("All assets loaded.")