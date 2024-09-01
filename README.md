# Interactive Learning Game

## Übersicht
Dieses Projekt ist ein interaktives Lernspiel, das mit Python und Pygame entwickelt wurde. Es zielt darauf ab, neue Mitarbeiter in einem Unternehmen durch ein spielerisches Onboarding-Erlebnis einzuführen.

## Hauptfunktionen
- Charaktererstellung mit individuellen Namen
- Interaktive Spielwelt mit NPCs und Objekten
- Quizsystem zur Überprüfung des Wissens
- Fortschrittssystem mit Erfahrungspunkten und Leveln
- Einfaches Inventarsystem

## Technische Details
- Entwickelt mit Python 3.x und Pygame
- Modulare Struktur mit verschiedenen Szenen (Hauptmenü, Charaktererstellung, Tutorial, Spielwelt, Quiz)
- Asset-Management-System für einfache Verwaltung von Grafiken, Sounds und Schriftarten
- Kamerasystem für eine scrollende Spielwelt
- Kollisionserkennung für Hindernisse und Interaktionen

## Installation und Ausführung
1. Stellen Sie sicher, dass Python 3.x installiert ist
2. Installieren Sie die erforderlichen Pakete: `pip install -r requirements.txt`
3. Führen Sie das Spiel aus: `python onboarding_game.py`

## Projektstruktur
- `onboarding_game.py`: Haupteinstiegspunkt des Spiels
- `game_engine.py`: Zentrale Spiellogik und -schleife
- `scenes/`: Enthält verschiedene Spielszenen (Hauptmenü, Charaktererstellung, etc.)
- `assets/`: Enthält Grafiken, Sounds und Schriftarten
- `config.py`: Konfigurationseinstellungen für das Spiel
- Verschiedene Hilfsklassen (Player, NPC, Camera, etc.)

## Aktueller Stand
- Grundlegende Spielmechaniken implementiert
- Charakterbewegung und Kameraverfolgung funktionieren
- Kollisionserkennung für Hindernisse implementiert
- Quizsystem grundlegend funktionsfähig
- Debugging-Ausgaben für einfachere Entwicklung hinzugefügt

## Nächste Schritte
- Verfeinerung der Spielerinteraktionen
- Erweiterung des Quizsystems
- Hinzufügen von mehr Inhalten (NPCs, Objekte, Fragen)
- Verbesserung der visuellen Darstellung
- Implementierung von Soundeffekten und Musik

## Mitwirkende
Siehe CONTRIBUTING.md für Informationen, wie Sie zum Projekt beitragen können.

## Lizenz
[Ihre gewählte Lizenz hier einfügen]