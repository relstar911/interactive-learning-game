import pygame
from content.asset_config import get_sprite_path, get_sound_path, SPRITE_MAPPINGS, SOUND_MAPPINGS, FONTS_DIR, get_font_path
from logger import logger
import os

class AssetManager:
    def __init__(self):
        self.sprites = {}
        self.sounds = {}
        self.fonts = {}
        self.load_assets()

    def load_assets(self):
        self.load_sprites()
        self.load_sounds()
        self.load_fonts()

    def load_sprites(self):
        for sprite_name in SPRITE_MAPPINGS:
            sprite_path = get_sprite_path(sprite_name)
            if sprite_path:
                try:
                    self.sprites[sprite_name] = pygame.image.load(sprite_path).convert_alpha()
                    logger.info(f"Loaded sprite: {sprite_name}")
                except pygame.error as e:
                    logger.error(f"Failed to load sprite {sprite_name}: {e}")
                    self.sprites[sprite_name] = self.create_placeholder_sprite()
            else:
                logger.warning(f"Sprite path not found for: {sprite_name}")
                self.sprites[sprite_name] = self.create_placeholder_sprite()

    def create_placeholder_sprite(self):
        surface = pygame.Surface((50, 50))
        surface.fill((255, 0, 255))  # Magenta color for missing sprites
        return surface

    def load_sounds(self):
        for sound_name in SOUND_MAPPINGS:
            sound_path = get_sound_path(sound_name)
            if sound_path:
                try:
                    self.sounds[sound_name] = pygame.mixer.Sound(sound_path)
                    logger.info(f"Loaded sound: {sound_name}")
                except pygame.error as e:
                    logger.error(f"Failed to load sound {sound_name}: {e}")
            else:
                logger.warning(f"Sound path not found for: {sound_name}")

    def load_fonts(self):
        font_sizes = [16, 24, 32, 48]
        styles = ['regular', 'bold']
        for size in font_sizes:
            for style in styles:
                font_name = f'raleway_{size}'
                if style == 'bold':
                    font_name += '_bold'
                font_path = get_font_path(f'raleway_{style}')
                if font_path and os.path.exists(font_path):
                    try:
                        self.fonts[font_name] = pygame.font.Font(font_path, size)
                        logger.info(f"Loaded font: {font_name}")
                    except pygame.error:
                        logger.error(f"Failed to load font: {font_name}")
                        self.fonts[font_name] = pygame.font.Font(None, size)
                else:
                    logger.warning(f"Font file not found: {font_path}. Using system default.")
                    self.fonts[font_name] = pygame.font.Font(None, size)

    def get_sprite(self, name):
        sprite = self.sprites.get(name)
        if sprite is None:
            logger.warning(f"Sprite '{name}' not found in asset manager.")
        return sprite

    def get_sound(self, name):
        return self.sounds.get(name)

    def get_font(self, name, size=24, style='regular'):
        font_name = f'{name}_{size}'
        if style == 'bold':
            font_name += '_bold'
        font = self.fonts.get(font_name)
        if font is None:
            logger.warning(f"Font '{font_name}' not found. Using system default.")
            font = pygame.font.Font(None, size)
        return font