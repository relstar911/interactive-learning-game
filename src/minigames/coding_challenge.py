import pygame

class CodingChallenge:
    def __init__(self, screen, font, challenge):
        self.screen = screen
        self.font = font
        self.challenge = challenge
        self.user_code = ""
        self.result = None

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.evaluate_code()
                return True
            elif event.key == pygame.K_BACKSPACE:
                self.user_code = self.user_code[:-1]
            else:
                self.user_code += event.unicode
        return False

    def evaluate_code(self):
        try:
            exec(self.user_code)
            result = eval("sum_two_numbers(3, 4)")
            if result == 7:
                self.result = "Correct!"
            else:
                self.result = f"Incorrect. Expected 7, got {result}"
        except Exception as e:
            self.result = f"Error: {str(e)}"

    def update(self, dt):
        # Hier können Sie Logik hinzufügen, die mit der verstrichenen Zeit zu tun hat
        pass

    def draw(self):
        self.screen.fill((255, 255, 255))
        challenge_text = self.font.render(self.challenge, True, (0, 0, 0))
        self.screen.blit(challenge_text, (10, 10))

        code_text = self.font.render(self.user_code, True, (0, 0, 0))
        self.screen.blit(code_text, (10, 50))

        if self.result:
            result_text = self.font.render(self.result, True, (0, 0, 0))
            self.screen.blit(result_text, (10, 90))

    def get_score(self):
        return 1 if self.result == "Correct!" else 0