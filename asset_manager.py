import pygame
from logger import logger
import os
from config import config

class AssetManager:
    def __init__(self):
        self.sprites = {}
        self.fonts = {}
        self.sounds = {}
        self.load_assets()

    def load_assets(self):
        # Laden und Skalieren der Sprites
        for name, file_path in config.sprite_files.items():
            try:
                if os.path.exists(file_path):
                    sprite = pygame.image.load(file_path).convert_alpha()
                    # Skalieren Sie das Sprite auf eine angemessene Größe
                    if name in ['player', 'npc']:
                        sprite = pygame.transform.scale(sprite, (64, 64))  # Beispielgröße für Charaktere
                    self.sprites[name] = sprite
                    logger.info(f"Loaded sprite: {name} from {file_path}")
                else:
                    logger.error(f"Sprite file not found: {file_path}")
            except pygame.error as e:
                logger.error(f"Konnte Sprite nicht laden: {file_path}. Fehler: {str(e)}")

        # Laden der Schriftarten
        for name, file_path in config.font_files.items():
            try:
                if os.path.exists(file_path):
                    for size in [24, 32, 48]:
                        self.fonts[f'{name}_{size}'] = pygame.font.Font(file_path, size)
                        logger.info(f"Loaded font: {name}_{size}")
                else:
                    logger.error(f"Font file not found: {file_path}")
            except pygame.error as e:
                logger.error(f"Konnte Schriftart nicht laden: {file_path}. Fehler: {str(e)}")

        # Laden der Sounds
        for name, file_path in config.sound_files.items():
            try:
                if os.path.exists(file_path):
                    self.sounds[name] = pygame.mixer.Sound(file_path)
                    logger.info(f"Loaded sound: {name}")
                else:
                    logger.error(f"Sound file not found: {file_path}")
            except pygame.error as e:
                logger.error(f"Konnte Sound nicht laden: {file_path}. Fehler: {str(e)}")

    def get_sprite(self, name):
        sprite = self.sprites.get(name)
        if sprite is None:
            logger.warning(f"Sprite '{name}' nicht gefunden. Verwende Fallback-Sprite.")
            fallback_sprite = pygame.Surface((64, 64))
            fallback_sprite.fill((255, 0, 255))  # Magenta als Fallback-Farbe
            return fallback_sprite
        return sprite

    def get_font(self, name, size, style='regular'):
        font = self.fonts.get(f'{style}_{size}')
        if font is None:
            logger.warning(f"Font '{style}_{size}' nicht gefunden. Verwende Standardschriftart.")
            font = pygame.font.Font(None, size)
        return font

    def get_sound(self, name):
        sound = self.sounds.get(name)
        if sound is None:
            logger.warning(f"Sound '{name}' nicht gefunden.")
        return sound