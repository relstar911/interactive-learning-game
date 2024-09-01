import pygame
from logger import logger

class SoundManager:
    def __init__(self, asset_manager):
        self.asset_manager = asset_manager

    def load_sound(self, sound_path):
        try:
            return pygame.mixer.Sound(sound_path)
        except pygame.error as e:
            logger.error(f"Failed to load sound: {sound_path}. Error: {e}")
            return None

    def play_effect(self, sound_name):
        sound = self.asset_manager.get_sound(sound_name)
        if sound:
            sound.play()
        else:
            logger.warning(f"Sound effect '{sound_name}' not found")

    def play_music(self, music_name):
        music = self.asset_manager.get_sound(music_name)
        if music:
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(-1)  # -1 bedeutet Endlosschleife
        else:
            logger.warning(f"Music '{music_name}' not found")

    def stop_music(self):
        pygame.mixer.music.stop()