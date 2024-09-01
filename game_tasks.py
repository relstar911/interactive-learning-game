from quiz import Quiz
from role_play_game import RolePlayGame
from team_leadership_game import TeamLeadershipGame
from logger import logger
from content.game_content import HR_QUESTIONS, IT_SCENARIOS, TEAM_LEAD_SCENARIOS
from content.asset_config import SPRITE_MAPPINGS

class GameTasks:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.tasks = {
            "HR Manager": self.hr_manager_task,
            "IT Specialist": self.it_specialist_task,
            "Team Lead": self.team_lead_task
        }

    def get_task_for_npc(self, npc_name):
        logger.debug(f"Getting task for NPC: {npc_name}")
        return self.tasks.get(npc_name, self.default_task)

    def hr_manager_task(self):
        logger.debug("Starting HR Manager task")
        return Quiz(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'), HR_QUESTIONS)

    def it_specialist_task(self):
        logger.debug("Starting IT Specialist task")
        return RolePlayGame(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'), IT_SCENARIOS)

    def team_lead_task(self):
        logger.debug("Starting Team Lead task")
        return TeamLeadershipGame(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'), TEAM_LEAD_SCENARIOS)

    def default_task(self):
        logger.warning("No specific task found for this NPC. Starting default quiz.")
        return Quiz(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'), HR_QUESTIONS[:2])

    # ... (Rest der Klasse bleibt unverändert)