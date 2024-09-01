import pygame
from config import config
import os

class SoundManager:
    def __init__(self, asset_manager):
        self.asset_manager = asset_manager
        self.current_music = None

    def play_background_music(self, music_name='telecom'):  # Ändern Sie den Standardwert zu 'telecom'
        music_path = self.asset_manager.get_sound(music_name)
        if music_path and os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)  # -1 für Endlosschleife
            self.current_music = music_name
        else:
            print(f"Warnung: Musikdatei '{music_name}' nicht gefunden.")

    def play_effect(self, effect_name):
        sound_path = self.asset_manager.get_sound(effect_name)
        if sound_path and os.path.exists(sound_path):
            sound = pygame.mixer.Sound(sound_path)
            sound.play()
        else:
            print(f"Warnung: Soundeffekt '{effect_name}' nicht gefunden.")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music = None