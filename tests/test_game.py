import unittest
from unittest.mock import Mock, patch
from game_engine import GameEngine  # Angenommen, Ihre Hauptspiellogik ist in game_engine.py
from player import Player
from inventory import Inventory, Item
from quiz import QuizSystem, Question

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = GameEngine()  # Verwenden Sie die richtige Klasse hier

    def test_game_initialization(self):
        self.assertIsNotNone(self.game.player)
        self.assertIsNotNone(self.game.current_scene)

    @patch('pygame.event.get')
    def test_game_update(self, mock_event_get):
        mock_event_get.return_value = []
        self.game.update()
        # Add assertions to check if the game state updates correctly

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player")

    def test_player_movement(self):
        initial_x = self.player.x
        initial_y = self.player.y
        self.player.move(1, 0)
        self.assertGreater(self.player.x, initial_x)
        self.assertEqual(self.player.y, initial_y)

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.test_item = Item("Test Item", "A test item", "test_image.png")

    def test_add_item(self):
        self.assertTrue(self.inventory.add_item(self.test_item))
        self.assertIn(self.test_item, self.inventory.items)

    def test_remove_item(self):
        self.inventory.add_item(self.test_item)
        self.assertTrue(self.inventory.remove_item(self.test_item))
        self.assertNotIn(self.test_item, self.inventory.items)

class TestQuizSystem(unittest.TestCase):
    def setUp(self):
        self.quiz_system = QuizSystem(Mock())

    def test_generate_quiz(self):
        mock_progress = Mock()
        mock_progress.skills = {"topic1": 1, "topic2": 2}
        quiz = self.quiz_system.generate_quiz(mock_progress)
        self.assertIsNotNone(quiz)
        self.assertTrue(len(quiz.questions) > 0)

if __name__ == '__main__':
    unittest.main()