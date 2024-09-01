class TutorialManager:
    def __init__(self, game):
        self.game = game
        self.steps = [
            TutorialStep("Willkommen", "Drücke SPACE zum Fortfahren"),
            TutorialStep("Bewegung", "Benutze WASD zum Bewegen", self.check_movement),
            TutorialStep("Interaktion", "Drücke E, um mit NPCs zu sprechen", self.check_interaction),
            # Weitere Schritte hinzufügen
        ]
        self.current_step = 0

    def update(self):
        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            if step.check_completion(self.game):
                self.current_step += 1

    def draw(self, screen):
        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            # Zeichnen Sie hier die Tutorial-Anweisungen

    def check_movement(self, game):
        # Überprüfen Sie, ob der Spieler sich bewegt hat
        pass

    def check_interaction(self, game):
        # Überprüfen Sie, ob der Spieler mit einem NPC interagiert hat
        pass

class TutorialStep:
    def __init__(self, title, instruction, completion_check=None):
        self.title = title
        self.instruction = instruction
        self.completion_check = completion_check

    def check_completion(self, game):
        if self.completion_check:
            return self.completion_check(game)
        return True