# Grundlegende Spielkonfiguration
BASE_NPC_COUNT = 5  # Basisanzahl der NPCs pro Level
LEVELS = 3  # Anzahl der Levels im Spiel

# NPC-Rollen und ihre relative Häufigkeit
NPC_ROLES = {
    "HR Manager": 0.2,
    "IT Specialist": 0.3,
    "Team Lead": 0.2,
    "Coworker": 0.3
}

# Level-spezifische Konfigurationen
LEVEL_CONFIGS = {
    1: {
        "npc_multiplier": 1,
        "difficulty": "easy",
        "available_areas": ["Office", "Meeting Room"],
    },
    2: {
        "npc_multiplier": 1.5,
        "difficulty": "medium",
        "available_areas": ["Office", "Meeting Room", "Cafeteria"],
    },
    3: {
        "npc_multiplier": 2,
        "difficulty": "hard",
        "available_areas": ["Office", "Meeting Room", "Cafeteria", "IT Department"],
    }
}

def get_npc_count(level):
    return int(BASE_NPC_COUNT * LEVEL_CONFIGS[level]["npc_multiplier"])

def get_npc_distribution(level):
    total_npcs = get_npc_count(level)
    distribution = {}
    for role, ratio in NPC_ROLES.items():
        distribution[role] = int(total_npcs * ratio)
    return distribution