import unittest
from kalah import Kalah


class KalahTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Kalah(6, 4)
        self.game1 = Kalah(5, 5)

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.game.kalah_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.assertEqual(self.game1.kalah_board, [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0])

    def test_illegal_hole(self):
        self.assertEqual(self.game.kalah_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.game.play(6)
        self.assertEqual(self.game.kalah_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])

        self.assertEqual(self.game1.kalah_board, [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0])
        self.game.play(-5)
        self.assertEqual(self.game1.kalah_board, [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0])

    def test_simple_move(self):
        self.assertEqual(self.game.kalah_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.game.play(0)
        self.assertEqual(self.game.kalah_board, [0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0])

    def test_cross_move(self):
        self.assertEqual(self.game.player_turn, True)
        self.assertEqual(self.game.kalah_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.game.play(2)
        self.assertEqual(self.game.kalah_board, [4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0])
        self.assertEqual(self.game.player_turn, True)

        self.game.play(5)
        self.assertEqual(self.game.kalah_board, [4, 4, 0, 5, 5, 0, 2, 5, 5, 5, 5, 4, 4, 0])


if __name__ == '__main__':
    unittest.main()
