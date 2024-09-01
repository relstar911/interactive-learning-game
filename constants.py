import os

# Basispfad des Projekts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Pfade zu verschiedenen Ordnern
SPRITES_DIR = os.path.join(BASE_DIR, 'sprites')
ASSETS_DIR = os.path.join(SPRITES_DIR, 'assets')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')
FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')
SCENES_DIR = os.path.join(BASE_DIR, 'scenes')

# Überprüfen Sie, ob die Verzeichnisse existieren
for directory in [SPRITES_DIR, ASSETS_DIR, SOUNDS_DIR, FONTS_DIR]:
    if not os.path.exists(directory):
        print(f"Warning: Directory does not exist: {directory}")
    else:
        print(f"Directory exists: {directory}")
        print(f"Contents of {directory}:")
        for item in os.listdir(directory):
            print(f"  - {item}")