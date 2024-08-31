# Interactive Learning Game

Ein Pygame-basiertes Lernspiel für Onboarding und Schulungen.

## Projektbeschreibung

Dieses Spiel dient als interaktive Plattform für Onboarding und Schulungen. Es bietet eine spielerische Umgebung, in der Benutzer durch verschiedene Levels navigieren, Quizze beantworten und Mini-Spiele spielen, um Wissen zu erwerben und zu festigen.

## Funktionen

- Charaktererstellung mit Namenseingabe
- Interaktive Spielwelt mit NPCs und Objekten
- Quiz-System mit dynamischen Fragen
- Memory-Mini-Spiel
- Inventarsystem für gesammelte Gegenstände
- Fortschrittsverfolgung und Levelaufstiege
- LLM-Integration für dynamische NPC-Interaktionen
- Pausefunktion im Spiel
- Asset-Management-System für Sprites, Sounds und Musik
- Verschiedene Spielszenen (Hauptmenü, Charaktererstellung, Tutorial, Spielwelt, Quiz, Mini-Spiel)

## Installation

1. Stellen Sie sicher, dass Python 3.x installiert ist.
2. Klonen Sie dieses Repository:
   ````
   git clone https://github.com/yourusername/interactive-learning-game.git
   ```
3. Navigieren Sie zum Projektverzeichnis:
   ````
   cd interactive-learning-game
   ```
4. Erstellen Sie eine virtuelle Umgebung:
   ````
   python -m venv venv
   ```
5. Aktivieren Sie die virtuelle Umgebung:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
6. Installieren Sie die erforderlichen Pakete:
   ````
   pip install -r requirements.txt
   ```
7. Erstellen Sie eine `.env` Datei im Hauptverzeichnis und fügen Sie Ihren OpenAI API-Schlüssel hinzu:
   ````
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Verwendung

Führen Sie das Hauptskript aus, um das Spiel zu starten: