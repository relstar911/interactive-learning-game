import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')

SPRITE_DIRS = {
    'characters': os.path.join(IMAGES_DIR, 'characters'),
    'items': os.path.join(IMAGES_DIR, 'items'),
    'tiles': os.path.join(IMAGES_DIR, 'tiles'),
    'ui': os.path.join(IMAGES_DIR, 'ui')
}

SPRITE_MAPPINGS = {
    'player': 'player.png',
    'npc': 'slime.png',
    'chest': 'chest_01.png',
    'rock': 'rock_in_water_01-sheet.png',
    'fence': 'fences.png',
    'dust': 'dust_particles_01.png',
    'book': 'book.png',
    'potion': 'potion.png',
    'tilemap': 'TX Tileset Grass.png',
}

SOUND_DIR = os.path.join(ASSETS_DIR, 'sounds')

SOUND_MAPPINGS = {
    'background_music': '1350180_TeleCom-INC.mp3',
    'menu_music': '1354018_288-Autograph-Piano-2023.mp3',
    'pickup': 'item-equip-6904.mp3',
}

MUSIC_DIR = os.path.join(ASSETS_DIR, 'music')

FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')

FONT_MAPPINGS = {
    'raleway_regular': 'Raleway-Regular.ttf',
    'raleway_bold': 'Raleway-Bold.ttf',
}

def get_sprite_path(sprite_name):
    if sprite_name in SPRITE_MAPPINGS:
        for category, sprite_dir in SPRITE_DIRS.items():
            full_path = os.path.join(sprite_dir, SPRITE_MAPPINGS[sprite_name])
            if os.path.exists(full_path):
                return full_path
    return None

def get_sound_path(sound_name):
    if sound_name in SOUND_MAPPINGS:
        return os.path.join(SOUND_DIR, SOUND_MAPPINGS[sound_name])
    return None

def get_music_path(music_name):
    if music_name in SOUND_MAPPINGS:  # Assuming music files are also in SOUND_MAPPINGS
        return os.path.join(MUSIC_DIR, SOUND_MAPPINGS[music_name])
    return None

def get_font_path(font_name):
    if font_name in FONT_MAPPINGS:
        return os.path.join(FONTS_DIR, FONT_MAPPINGS[font_name])
    return None

def debug_sound_paths():
    print(f"SOUND_DIR: {SOUND_DIR}")
    print(f"Files in SOUND_DIR: {os.listdir(SOUND_DIR)}")
    for sound_name, file_name in SOUND_MAPPINGS.items():
        full_path = os.path.join(SOUND_DIR, file_name)
        print(f"{sound_name}: {'Exists' if os.path.exists(full_path) else 'Not Found'} - {full_path}")

def debug_music_paths():
    print(f"MUSIC_DIR: {MUSIC_DIR}")
    print(f"Files in MUSIC_DIR: {os.listdir(MUSIC_DIR)}")
    for music_name, file_name in SOUND_MAPPINGS.items():  # Assuming music files are also in SOUND_MAPPINGS
        full_path = os.path.join(MUSIC_DIR, file_name)
        print(f"{music_name}: {'Exists' if os.path.exists(full_path) else 'Not Found'} - {full_path}")