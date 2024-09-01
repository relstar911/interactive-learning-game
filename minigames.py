from quiz import Quiz
from role_play_game import RolePlayGame
from team_leadership_game import TeamLeadershipGame
from memory_game import MemoryGame
from coding_challenge import CodingChallenge
from company_bingo import CompanyBingo
from puzzle_game import PuzzleGame
from logger import logger

class MinigameManager:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.current_game = None

    def start_game(self, game_type, *args):
        if game_type == "quiz":
            self.current_game = Quiz(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'), *args)
        elif game_type == "role_play":
            self.current_game = RolePlayGame(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'), *args)
        elif game_type == "team_leadership":
            self.current_game = TeamLeadershipGame(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'), *args)
        elif game_type == "memory":
            self.current_game = MemoryGame(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'))
        elif game_type == "coding_challenge":
            self.current_game = CodingChallenge(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'), *args)
        elif game_type == "company_bingo":
            self.current_game = CompanyBingo(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'), *args)
        elif game_type == "puzzle":
            self.current_game = PuzzleGame(self.game_engine.screen, self.game_engine.asset_manager.get_font('raleway', 24, 'regular'))
        else:
            logger.error(f"Unknown game type: {game_type}")
            return None
        
        logger.info(f"Started minigame: {game_type}")
        return self.current_game

    def end_game(self):
        score = self.current_game.get_score()
        self.current_game = None
        return score

    def update(self, dt):
        if self.current_game:
            return self.current_game.update(dt)
        return None

    def render(self, screen):
        if self.current_game:
            self.current_game.render(screen)

    def handle_event(self, event):
        if self.current_game:
            return self.current_game.handle_event(event)
        return False