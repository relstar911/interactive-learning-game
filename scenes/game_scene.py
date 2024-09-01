from npc import NPC  # Importieren der NPC-Klasse

def create_npcs(asset_manager):
    npc1 = NPC("NPC1", (100, 150), "Willkommen in unserer Welt! Viel Spaß beim Lernen.", "npc_sprite")
    npc2 = NPC("NPC2", (200, 250), "Hast du schon das Quiz ausprobiert?", "npc_sprite")
    npc1.load_sprite(asset_manager)
    npc2.load_sprite(asset_manager)
    return [npc1, npc2]

class GameScene:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.npcs = create_npcs(game_engine.asset_manager)
        # ... bestehender Code ...