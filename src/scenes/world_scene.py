import pygame
from src.entities.player import Player
from src.entities.npc import NPC
from src.core.quest_manager import QuestManager
from content.game_content import ALL_LEVELS_CONTENT, INTERACTIVE_OBJECTS, ONBOARDING_PROGRESS
from src.ui.dialogue_box import DialogueBox
from content.game_config import get_npc_distribution
import random

class WorldScene:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.player = Player(400, 300)
        self.quest_manager = QuestManager()
        self.current_level = 1
        self.npcs = self.generate_npcs()
        print(f"Generated {len(self.npcs)} NPCs")  # Debug print
        self.interactive_objects = self.generate_interactive_objects()
        self.dialogue_box = None
        self.interaction_cooldowns = {}
        self.progress = {area: 0 for area in ONBOARDING_PROGRESS.keys()}

    def generate_npcs(self):
        npcs = []
        npc_distribution = get_npc_distribution(self.current_level)
        for role, count in npc_distribution.items():
            for i in range(count):
                x = random.randint(50, 950)
                y = random.randint(50, 950)
                npc = NPC(x, y, f"{role}_{i+1}", role)
                npcs.append(npc)
        return npcs

    def generate_interactive_objects(self):
        return [pygame.Rect(obj['position'][0], obj['position'][1], 40, 40) for obj in INTERACTIVE_OBJECTS]

    def handle_event(self, event):
        if self.dialogue_box:
            dialogue_over = self.dialogue_box.handle_event(event)
            if dialogue_over:
                self.dialogue_box = None
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_engine.scene_manager.set_scene("main_menu")
                elif event.key == pygame.K_SPACE:
                    self.check_npc_interaction()
        self.player.handle_event(event)

    def update(self, dt):
        self.player.update(dt)
        for npc in self.npcs:
            npc.update(dt)
        self.check_npc_collision()
        self.check_object_interaction()

    def render(self, screen):
        screen.fill((200, 200, 200))
        for obj in self.interactive_objects:
            pygame.draw.rect(screen, (0, 255, 0), obj)
        for npc in self.npcs:
            npc.render(screen)
        self.player.render(screen)
        if self.dialogue_box:
            self.dialogue_box.render(screen)
        self.render_progress(screen)

    def check_npc_interaction(self):
        for npc in self.npcs:
            if self.player.rect.colliderect(npc.rect):
                self.start_dialogue(npc)
                break

    def check_npc_collision(self):
        for npc in self.npcs:
            if self.player.rect.colliderect(npc.rect) and not self.dialogue_box:
                print(f"Collided with NPC: {npc.name}")  # Debug print
                self.start_dialogue(npc)

    def check_object_interaction(self):
        for i, obj in enumerate(self.interactive_objects):
            if self.player.rect.colliderect(obj):
                self.interact_with_object(INTERACTIVE_OBJECTS[i])

    def start_dialogue(self, npc):
        print(f"Starting dialogue with {npc.name}")  # Debug print
        dialogue_data = npc.get_dialogue()
        print(f"Dialogue data: {dialogue_data}")  # Debug print
        self.dialogue_box = DialogueBox(dialogue_data, self.end_dialogue, self.game_engine)

    def end_dialogue(self):
        print("Ending dialogue")  # Debug print
        self.dialogue_box = None

    def interact_with_object(self, object_data):
        current_time = pygame.time.get_ticks()
        if current_time - self.interaction_cooldowns.get(object_data['name'], 0) > 5000:  # 5 seconds cooldown
            print(f"Interacting with {object_data['name']}")
            self.interaction_cooldowns[object_data['name']] = current_time
            for area, value in object_data['knowledge_gain'].items():
                self.progress[area] += value
                print(f"Gained {value} knowledge in {area}")

    def render_progress(self, screen):
        font = pygame.font.Font(None, 24)
        y = 10
        for area, value in self.progress.items():
            text = font.render(f"{area}: {value}", True, (0, 0, 0))
            screen.blit(text, (10, y))
            y += 30
