import unittest
from kalah import Kalah


class KalahTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Kalah(6, 4)
        self.game1 = Kalah(5, 5)
        self.game2 = Kalah(4, 6)

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

    def test_two_simple_moves(self):
        self.assertEqual(self.game.player_turn, True)
        self.assertEqual(self.game.kalah_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.game.play(1)
        self.assertEqual(self.game.kalah_board, [4, 0, 5, 5, 5, 5, 0, 4, 4, 4, 4, 4, 4, 0])
        self.assertEqual(self.game.player_turn, False)
        self.game.play(1)
        self.assertEqual(self.game.kalah_board, [4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0])

    def test_player_2_crosses(self):
        self.test_two_simple_moves()
        self.assertEqual(self.game.player_turn, True)
        self.assertEqual(self.game.kalah_board, [4, 0, 5, 5, 5, 5, 0, 4, 0, 5, 5, 5, 5, 0])

        self.game.play(2)
        self.assertEqual(self.game.kalah_board, [4, 0, 0, 6, 6, 6, 1, 5, 0, 5, 5, 5, 5, 0])
        self.assertEqual(self.game.player_turn, False)

        self.game.play(2)
        self.assertEqual(self.game.kalah_board, [5, 0, 0, 6, 6, 6, 1, 5, 0, 0, 6, 6, 6, 1])
        self.assertEqual(self.game.player_turn, True)

    def test_cross_other_bank(self):
        self.assertEqual(self.game2.player_turn, True)
        self.assertEqual(self.game2.kalah_board, [6, 6, 6, 6, 0, 6, 6, 6, 6, 0])
        self.game2.play(3)
        self.assertEqual(self.game2.kalah_board, [7, 6, 6, 0, 1, 7, 7, 7, 7, 0])
        self.assertEqual(self.game2.player_turn, False)

    def test_empty_hole(self):
        self.assertEqual(self.game.player_turn, True)
        self.assertEqual(self.game.kalah_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.game.play(2)
        self.assertEqual(self.game.kalah_board, [4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0])
        self.assertEqual(self.game.player_turn, True)
        self.game.play(2)
        self.assertEqual(self.game.kalah_board, [4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0])
        self.assertEqual(self.game.player_turn, True)

    def test_bonus_move_player_1(self):
        self.assertEqual(self.game.player_turn, True)
        self.assertEqual(self.game.kalah_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.game.play(2)
        self.assertEqual(self.game.kalah_board, [4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0])
        self.assertEqual(self.game.player_turn, True)

    def test_bonus_move_player_2(self):
        self.assertEqual(self.game.player_turn, True)
        self.assertEqual(self.game.kalah_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.game.play(0)
        self.assertEqual(self.game.kalah_board, [0, 5, 5, 5, 5, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.assertEqual(self.game.player_turn, False)
        self.game.play(2)
        self.assertEqual(self.game.kalah_board, [0, 5, 5, 5, 5, 4, 0, 4, 4, 0, 5, 5, 5, 1])
        self.assertEqual(self.game.player_turn, False)

    def test_Capture_player_1(self):
        self.game.kalah_board = [
            1, 0, 3, 4, 5, 6, 7,
            1, 2, 3, 4, 5, 6, 7,
        ]
        self.assertEqual(self.game.player_turn, True)
        self.assertEqual(
            self.game.kalah_board,
            [
                1, 0, 3, 4, 5, 6, 7,
                1, 2, 3, 4, 5, 6, 7,
            ])
        self.game.play(0)
        self.assertEqual(
            self.game.kalah_board,
            [
                0, 0, 3, 4, 5, 6, 10,
                1, 0, 3, 4, 5, 6, 7,
            ])
        self.assertEqual(self.game.player_turn, False)
        self.game.play(0)
        self.assertEqual(
            self.game.kalah_board,
            [
                0, 0, 3, 4, 5, 6, 10,
                0, 0, 3, 4, 5, 6, 8,
            ])


if __name__ == '__main__':
    unittest.main()
