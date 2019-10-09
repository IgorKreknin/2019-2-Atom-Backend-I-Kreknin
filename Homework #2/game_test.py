import unittest
import game


class TestGame(unittest.TestCase):

    def test_field_functions(self):
        my_game = game.game()
        my_game.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(my_game.check_field(), None)
        my_game.field = [['X', 'X', 'X'], ['X', 'O', ' '], [' ', ' ', ' ']]
        self.assertEqual(my_game.check_field(), 0)
        my_game.field = [['X', 'X', 'O'], ['X', 'O', ' '], ['O', ' ', ' ']]
        self.assertEqual(my_game.check_field(), 1)
        my_game.field = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertEqual(my_game.check_field(), 2)

    def test_validator(self):
        my_game = game.game()
        self.assertTrue(my_game.validate([2, 0]))
        self.assertTrue(my_game.validate(['0', '0']))
        self.assertFalse(my_game.validate([0]))
        self.assertFalse(my_game.validate([0, 1, 0]))
        self.assertFalse(my_game.validate(['0', 'str']))
        self.assertFalse(my_game.validate(['str']))

    def test_io(self):
        my_game = game.game()
        # self.assertEqual(my_game.read("1\t\t2"), ['1', '2'])
        # self.assertEqual(my_game.read('1\t\t2 3'), ['1', '2', '3'])
        # self.assertEqual(my_game.read("1 str\t4"), ['1', 'str', '4'])
        self.assertTrue(my_game.put([0, 0]))
        self.assertTrue(my_game.put(['1', '0']))
        self.assertFalse(my_game.put([0, -1]))
        self.assertFalse(my_game.put([0, 'str']))
        self.assertFalse(my_game.put([0, 0]))

    if __name__ == '__main__':
        unittest.main()
