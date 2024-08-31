interactive-learning-game/
│
├── assets/
│ ├── sprites/
│ │ ├── Texture/
│ │ │ ├── TX Player.png
│ │ │ ├── TX Props.png
│ │ │ ├── TX Tileset Grass.png
│ │ │ └── TX Plant.png
│ │ ├── prototype/
│ │ │ ├── tilesheet.png
│ │ │ └── tilesheet_complete.png
│ │ └── buildings/
│ │ ├── tilesheet.png
│ │ └── tilesheet_complete.png
│ ├── fonts/
│ │ └── Raleway/
│ │ ├── Raleway-Regular.ttf
│ │ ├── Raleway-Bold.ttf
│ │ └── Raleway-Italic.ttf
│ ├── sounds/
│ │ ├── pickup.wav
│ │ ├── interact.wav
│ │ └── levelup.wav
│ └── music/
│ └── background_music.mp3
│
├── scenes/
│ ├── init.py
│ ├── base_scene.py
│ ├── main_menu.py
│ ├── character_creation.py
│ ├── tutorial.py
│ ├── game_world.py
│ ├── quiz.py
│ └── mini_game.py
│
├── tests/
│ └── test_game_objects.py
│
├── .env
├── .gitignore
├── asset_manager.py
├── camera.py
├── config.py
├── config.json
├── CONTRIBUTING.md
├── game_engine.py
├── game_objects.py
├── game_states.py
├── inventory.py
├── llm_integration.py
├── logger.py
├── mini_game.py
├── npc.py
├── onboarding_game.py
├── player.py
├── progress.py
├── PROJECT_STATUS.md
├── PROJECT_STRUCTURE.md
├── quiz.py
├── README.md
├── requirements.txt
└── sprites.py

## Hauptdateien und ihre Funktionen

- `onboarding_game.py`: Haupteinstiegspunkt des Spiels
- `game_engine.py`: Zentrale Spielengine-Klasse
- `asset_manager.py`: Verwaltet das Laden und Zugreifen auf Assets
- `config.py` und `config.json`: Konfigurationseinstellungen für das Spiel
- `player.py`: Implementiert die Spielerklasse
- `npc.py`: Implementiert die NPC-Klasse
- `game_objects.py`: Definiert verschiedene Spielobjekte
- `inventory.py`: Implementiert das Inventarsystem
- `quiz.py`: Enthält die Quizlogik
- `mini_game.py`: Implementiert das Memory-Mini-Spiel
- `llm_integration.py`: Integriert die OpenAI-API für NPC-Dialoge
- `camera.py`: Implementiert die Kamerafunktionalität für die Spielwelt
- `progress.py`: Verwaltet den Spielerfortschritt
- `game_states.py`: Definiert die verschiedenen Spielzustände
- `logger.py`: Implementiert das Logging-System

## Szenen

- `base_scene.py`: Basisklasse für alle Szenen
- `main_menu.py`: Hauptmenü-Szene
- `character_creation.py`: Charaktererstellungs-Szene
- `tutorial.py`: Tutorial-Szene
- `game_world.py`: Hauptspielwelt-Szene
- `quiz.py`: Quiz-Szene
- `mini_game.py`: Mini-Spiel-Szene

## Assets

Das Spiel verwendet verschiedene Assets, die in den entsprechenden Unterordnern des `assets/`-Verzeichnisses organisiert sind:

- Sprites: Texturen, Prototypen und Gebäude
- Schriftarten: Raleway-Schriftfamilie
- Sounds: Soundeffekte für verschiedene Spielaktionen
- Musik: Hintergrundmusik für das Spiel

## Tests

- `test_game_objects.py`: Enthält Unit-Tests für Spielobjekte

## Konfiguration und Umgebung

- `.env`: Enthält sensible Konfigurationsdaten (nicht im Repository enthalten)
- `.gitignore`: Konfiguration für Git-Versionskontrolle
- `requirements.txt`: Liste der Python-Abhängigkeiten

## Dokumentation

- `README.md`: Projektübersicht und Installationsanweisungen
- `CONTRIBUTING.md`: Richtlinien für Beiträge zum Projekt
- `PROJECT_STATUS.md`: Aktueller Projektstatus und nächste Schritte
- `PROJECT_STRUCTURE.md`: Diese Datei, die die Projektstruktur beschreibt