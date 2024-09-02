import os
from content.game_content import (
    HR_QUESTIONS, IT_SCENARIOS, NPCS, NPC_DIALOGUES, GAME_OBJECTS,
    WORLD_CONFIG, PLAYER_INITIAL_CONFIG, TEAM_LEAD_SCENARIOS,
    ONBOARDING_PROGRESS, MINIGAME_REWARDS, INTERACTIVE_OBJECTS,
    TEAM_LEAD_FACTS, CHARACTERS
)
from content.game_config import (
    BASE_NPC_COUNT, LEVELS, NPC_ROLES, LEVEL_CONFIGS,
    get_npc_count, get_npc_distribution
)
from content.config import Config

# Game content
HR_QUESTIONS = HR_QUESTIONS
IT_SCENARIOS = IT_SCENARIOS
NPCS = NPCS
NPC_DIALOGUES = NPC_DIALOGUES
GAME_OBJECTS = GAME_OBJECTS
WORLD_CONFIG = WORLD_CONFIG
PLAYER_INITIAL_CONFIG = PLAYER_INITIAL_CONFIG
TEAM_LEAD_SCENARIOS = TEAM_LEAD_SCENARIOS
ONBOARDING_PROGRESS = ONBOARDING_PROGRESS
MINIGAME_REWARDS = MINIGAME_REWARDS
INTERACTIVE_OBJECTS = INTERACTIVE_OBJECTS
TEAM_LEAD_FACTS = TEAM_LEAD_FACTS
CHARACTERS = CHARACTERS

# Game configuration
BASE_NPC_COUNT = BASE_NPC_COUNT
LEVELS = LEVELS
NPC_ROLES = NPC_ROLES
LEVEL_CONFIGS = LEVEL_CONFIGS

# Helper functions
get_npc_count = get_npc_count
get_npc_distribution = get_npc_distribution

# Load configuration
config = Config()

# Game window configuration
WINDOW_WIDTH = config.window_width
WINDOW_HEIGHT = config.window_height
WINDOW_TITLE = config.window_title
FPS = config.fps

# Player configuration
PLAYER_SPEED = config.player_speed
MAX_PLAYER_NAME_LENGTH = config.max_player_name_length

# Asset paths
BASE_DIR = config.base_dir
SPRITE_DIR = config.sprite_dir
CHARACTER_DIR = config.character_dir
ASSET_DIR = config.asset_dir
FONT_DIR = config.font_dir
SOUND_DIR = config.sound_dir
TEXTURE_DIR = config.texture_dir

# OpenAI API Key
OPENAI_API_KEY = config.openai_api_key

# Logging configuration
LOG_LEVEL = 'DEBUG'