from logger import logger

class SceneManager:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.scenes = {}
        self.current_scene = None
        self.scene_stack = []

    def add_scene(self, state, scene):
        self.scenes[state] = scene

    def set_scene(self, state):
        if state in self.scenes:
            if self.current_scene:
                self.scene_stack.append(self.current_scene)
            self.current_scene = self.scenes[state]
            self.current_scene.enter()
            logger.info(f"Changed to scene: {state}")
        else:
            logger.error(f"Scene {state} not found")

    def pop_scene(self):
        if self.scene_stack:
            self.current_scene = self.scene_stack.pop()
            self.current_scene.enter()
            logger.info(f"Returned to previous scene")
        else:
            logger.warning("No previous scene to return to")

    def update(self, dt):
        if self.current_scene:
            self.current_scene.update(dt)

    def render(self, screen):
        if self.current_scene:
            self.current_scene.render(screen)

    def handle_event(self, event):
        if self.current_scene:
            self.current_scene.handle_event(event)