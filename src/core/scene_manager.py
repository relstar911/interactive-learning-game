class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def set_scene(self, name):
        if name in self.scenes:
            self.current_scene = self.scenes[name]
        else:
            raise ValueError(f"Scene '{name}' not found")

    def update(self, dt):
        if self.current_scene:
            self.current_scene.update(dt)

    def render(self, screen):
        if self.current_scene:
            self.current_scene.render(screen)

    def handle_event(self, event):
        if self.current_scene:
            self.current_scene.handle_event(event)
