# AssetManager (asset_manager.py)

## Klasse: AssetManager

### Attribute
- sprites: Dict[str, pygame.Surface]
- prototype_sprites: Dict[str, pygame.Surface]
- building_sprites: Dict[str, pygame.Surface]
- fonts: Dict[str, pygame.font.Font]
- sounds: Dict[str, pygame.mixer.Sound]
- music: Dict[str, str]

### Methoden
- load_all_assets(): Lädt alle Assets
- load_all_sprites(): Lädt alle Sprite-Assets
- load_all_prototype_sprites(): Lädt Prototype-Sprites
- load_all_building_sprites(): Lädt Building-Sprites
- load_sprite(name, filename, category, target_dict=None): Lädt ein einzelnes Sprite
- load_all_fonts(): Lädt alle Schriftarten
- load_font(name, filename, size=36): Lädt eine einzelne Schriftart
- load_all_sounds(): Lädt alle Soundeffekte
- load_sound(name, filename): Lädt einen einzelnen Soundeffekt
- load_all_music(): Lädt alle Musikstücke
- load_music(name, filename): Lädt ein einzelnes Musikstück
- extract_sprite(sheet, x, y, width, height): Extrahiert ein Sprite aus einem Spritesheet
- get_sprite(name, category='texture'): Gibt ein Sprite zurück
- play_sound(name): Spielt einen Soundeffekt ab
- play_music(name): Spielt ein Musikstück ab
- create_placeholder_image(width, height, color): Erstellt ein Platzhalterbild
- get_color_for_sprite(name): Gibt eine Farbe für ein Platzhalter-Sprite zurück
- get_font(name, size=36): Gibt eine Schriftart zurück

## Globale Instanz
asset_manager: AssetManager