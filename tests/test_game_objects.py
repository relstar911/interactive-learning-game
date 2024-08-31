import unittest
from game_objects import GameObject
from player import Player

class TestGameObjects(unittest.TestCase):
    def test_interact(self):
        player = Player("Test", 0, 0)
        obj = GameObject(0, 0, "test", "Test Object", "A test object")
        message = obj.interact(player)
        self.assertIn("Test Object", message)
        self.assertEqual(len(player.inventory.items), 1)
        self.assertEqual(player.inventory.items[0].name, "Test Object")

if __name__ == '__main__':
    unittest.main()