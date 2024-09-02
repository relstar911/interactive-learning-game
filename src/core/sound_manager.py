import pygame
from pygame import mixer
from src.utils.logger import logger  # Korrigierter Import

class SoundManager:
    def __init__(self):
        mixer.init()
        self.sounds = {}
        self.music = None

    def load_sound(self, name, file_path):
        self.sounds[name] = mixer.Sound(file_path)

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()
        else:
            logger.warning(f"Sound {name} not found")

    def load_music(self, file_path):
        self.music = file_path

    def play_music(self, loops=-1):
        if self.music:
            mixer.music.load(self.music)
            mixer.music.play(loops)
        else:
            logger.warning("No music loaded")

    def stop_music(self):
        mixer.music.stop()
