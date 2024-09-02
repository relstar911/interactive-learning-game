import pygame
from src.core.minigames import Minigames

class DialogueBox:
    def __init__(self, dialogue_data, end_callback, game_engine):
        self.dialogue_data = dialogue_data
        self.end_callback = end_callback
        self.game_engine = game_engine
        self.font = pygame.font.Font(None, 32)
        self.current_text = dialogue_data['greeting']
        self.text_surface = self.font.render(self.current_text, True, (255, 255, 255))
        self.options = dialogue_data['options']
        self.option_surfaces = [self.font.render(option["text"], True, (255, 255, 255)) for option in self.options]
        self.selected_option = 0
        self.minigames = game_engine.minigames

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                self.next()
            elif event.key == pygame.K_ESCAPE:
                self.end_callback()
        return False  # Dialogue is not over

    def next(self):
        if len(self.options) > 0:
            selected_option = self.options[self.selected_option]
            print(f"Selected option: {selected_option}")  # Debug print
            if "response" in selected_option:
                self.current_text = selected_option["response"]
                self.text_surface = self.font.render(self.current_text, True, (255, 255, 255))
                self.options = selected_option.get("follow_up", [])
                if not self.options:
                    self.options = [{"text": "End conversation", "end_dialogue": True}]
                self.option_surfaces = [self.font.render(option["text"], True, (255, 255, 255)) for option in self.options]
                self.selected_option = 0
            elif "minigame" in selected_option:
                self.launch_minigame(selected_option["minigame"])
            elif "end_dialogue" in selected_option or "start_game" in selected_option:
                if "start_game" in selected_option and selected_option["start_game"]:
                    self.launch_minigame(selected_option.get("minigame", "it_problem_solving"))
                else:
                    self.end_callback()
        else:
            self.end_callback()

    def launch_minigame(self, minigame_name):
        print(f"Launching minigame: {minigame_name}")  # Debug print
        if minigame_name == "hr_quiz":
            self.game_engine.scene_manager.set_scene("hr_quiz")
        elif minigame_name == "it_problem_solving":
            self.game_engine.scene_manager.set_scene("it_quiz")
        else:
            minigame = self.minigames.get_minigame(minigame_name)
            if minigame:
                self.game_engine.scene_manager.set_scene("mini_game", minigame(self.game_engine.screen, self.font))
            else:
                print(f"Minigame not found: {minigame_name}")  # Debug print
        self.end_callback()  # End the dialogue when launching a mini-game

    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (50, 400, 700, 200))
        screen.blit(self.text_surface, (60, 410))
        for i, option_surface in enumerate(self.option_surfaces):
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            option_surface = self.font.render(self.options[i]["text"][:50], True, color)  # Limit text length
            screen.blit(option_surface, (60, 450 + i * 30))