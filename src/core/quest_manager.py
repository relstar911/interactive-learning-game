class Quest:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

class QuestManager:
    def __init__(self):
        self.quests = [
            Quest("Einführung", "Sprich mit dem HR Manager"),
            Quest("IT-Sicherheit", "Lerne die Grundlagen der IT-Sicherheit vom IT-Spezialisten")
        ]

    def update(self):
        # Hier könnten Sie die Fortschritte der Quests überprüfen
        pass

    def get_active_quests(self):
        return [quest for quest in self.quests if not quest.completed]

    def complete_quest(self, quest_name):
        for quest in self.quests:
            if quest.name == quest_name:
                quest.completed = True
                print(f"Quest abgeschlossen: {quest_name}")
                break