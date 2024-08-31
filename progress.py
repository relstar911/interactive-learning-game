class Achievement:
    def __init__(self, name, description, xp_reward):
        self.name = name
        self.description = description
        self.xp_reward = xp_reward
        self.completed = False

    def complete(self):
        self.completed = True
        return self.xp_reward

class ProgressTracker:
    def __init__(self):
        self.achievements = [
            Achievement("Erster Schritt", "Schließe das Tutorial ab", 50),
            Achievement("Wissensdurst", "Beantworte 5 Quizfragen richtig", 100),
            Achievement("Gedächtniskünstler", "Gewinne das Memory-Spiel", 150),
            Achievement("Sammler", "Sammle 3 verschiedene Gegenstände", 200),
            Achievement("Meisterschüler", "Erreiche Level 5", 500)
        ]

    def check_achievements(self, player):
        for achievement in self.achievements:
            if not achievement.completed:
                if self.check_condition(achievement, player):
                    xp_reward = achievement.complete()
                    player.gain_xp(xp_reward)
                    return f"Achievement freigeschaltet: {achievement.name}! +{xp_reward} XP"
        return None

    def check_condition(self, achievement, player):
        if achievement.name == "Erster Schritt":
            return player.tutorial_completed
        elif achievement.name == "Wissensdurst":
            return player.quiz_correct_answers >= 5
        elif achievement.name == "Gedächtniskünstler":
            return player.memory_game_won
        elif achievement.name == "Sammler":
            return len(player.get_inventory()) >= 3
        elif achievement.name == "Meisterschüler":
            return player.level >= 5
        return False