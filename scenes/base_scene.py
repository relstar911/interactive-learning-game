class BaseScene:
    def __init__(self, game_engine):
        self.game_engine = game_engine

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass