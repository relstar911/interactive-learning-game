import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPRITES_DIR = os.path.join(BASE_DIR, 'sprites')
ASSETS_DIR = os.path.join(SPRITES_DIR, 'assets')

SPRITE_DIRS = {
    'characters': os.path.join(SPRITES_DIR, 'characters'),
    'objects': os.path.join(SPRITES_DIR, 'objects'),
    'particles': os.path.join(SPRITES_DIR, 'particles'),
    'textures': os.path.join(ASSETS_DIR, 'Texture')
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

FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts', 'Raleway', 'static')

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

def get_font_path(font_name):
    if font_name in FONT_MAPPINGS:
        return os.path.join(FONTS_DIR, FONT_MAPPINGS[font_name])
    return None