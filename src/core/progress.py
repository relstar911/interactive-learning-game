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

class Progress:
    def __init__(self):
        self.level = 1
        self.xp = 0
        self.skills = {}
        self.achievements = []
        self.quests_completed = []

    def add_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_for_next_level():
            self.level_up()

    def level_up(self):
        self.level += 1
        # Benachrichtigung an den Spieler über den Levelaufstieg

    def xp_for_next_level(self):
        return self.level * 100  # Einfache Formel, kann angepasst werden

    def improve_skill(self, skill_name, amount):
        if skill_name not in self.skills:
            self.skills[skill_name] = 0
        self.skills[skill_name] += amount

    def complete_quest(self, quest_name):
        self.quests_completed.append(quest_name)
        # Überprüfen Sie hier auf mögliche Achievements

    def unlock_achievement(self, achievement_name):
        if achievement_name not in self.achievements:
            self.achievements.append(achievement_name)
            # Benachrichtigung an den Spieler über das freigeschaltete Achievement

    def get_progress_summary(self):
        return f"Level: {self.level}, XP: {self.xp}, Skills: {self.skills}, Quests: {len(self.quests_completed)}, Achievements: {len(self.achievements)}"