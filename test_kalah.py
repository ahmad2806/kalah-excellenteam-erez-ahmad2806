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

    def test_capture_player_1(self):
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
        self.assertEqual(self.game.player_turn, True)

    def test_illegal_capture(self):
        self.assertEqual(self.game.player_turn, True)
        self.game.kalah_board = [
            1, 2, 3, 1, 5, 3, 7,
            0, 0, 1, 0, 5, 6, 24,
        ]

        self.game.play(5)
        self.game.kalah_board = [
            1, 2, 3, 1, 5, 0, 8,
            1, 1, 1, 0, 5, 6, 24,
        ]
        self.assertEqual(self.game.player_turn, False)

    def test_no_capture_player(self):
        self.game.kalah_board = [
            1, 0, 3, 4, 5, 6, 7,
            1, 0, 3, 4, 5, 6, 7,
        ]
        self.assertEqual(self.game.player_turn, True)
        self.assertEqual(
            self.game.kalah_board,
            [
                1, 0, 3, 4, 5, 6, 7,
                1, 0, 3, 4, 5, 6, 7,
            ])
        self.game.play(0)
        self.assertEqual(
            self.game.kalah_board,
            [
                0, 1, 3, 4, 5, 6, 7,
                1, 0, 3, 4, 5, 6, 7,
            ])
        self.assertEqual(self.game.player_turn, False)

    def test_game_ends_and_player_1_capture(self):
        self.assertEqual(self.game.player_turn, True)
        self.game.kalah_board = [
            0, 0, 1, 0, 0, 0, 21,
            1, 2, 3, 1, 5, 6, 8,

        ]
        self.assertEqual(self.game.new_game_is_needed, False)
        self.game.play(2)
        self.assertEqual(self.game.kalah_board, [
            0, 0, 0, 0, 0, 0, 23,
            0, 0, 0, 0, 0, 0, 25,
        ])

        self.assertEqual(self.game.player_2, 1)
        self.assertEqual(self.game.player_1, 0)
        self.assertEqual(self.game.ties, 0)
        self.assertEqual(self.game.new_game_is_needed, True)

    def test_game_ends_and_player_2_capture(self):
        self.assertEqual(self.game.player_turn, True)
        self.game.kalah_board = [
            1, 2, 3, 1, 5, 6, 8,
            0, 0, 1, 0, 0, 0, 21,

        ]
        self.assertEqual(self.game.new_game_is_needed, False)
        self.game.player_turn = not self.game.player_turn
        self.game.play(2)
        self.assertEqual(self.game.kalah_board, [
            0, 0, 0, 0, 0, 0, 25,
            0, 0, 0, 0, 0, 0, 23,
        ])

        self.assertEqual(self.game.player_2, 0)
        self.assertEqual(self.game.player_1, 1)
        self.assertEqual(self.game.ties, 0)
        self.assertEqual(self.game.new_game_is_needed, True)

    def test_game_ends_and_tie(self):
        self.assertEqual(self.game.player_turn, True)
        self.game.kalah_board = [
            0, 1, 0, 0, 0, 0, 22,
            0, 0, 1, 0, 0, 0, 24,

        ]
        self.assertEqual(self.game.new_game_is_needed, False)
        self.game.play(1)
        self.game.kalah_board = [
            0, 0, 0, 0, 0, 0, 24,
            0, 0, 0, 0, 0, 0, 24,
        ]
        self.assertEqual(self.game.player_2, 0)
        self.assertEqual(self.game.player_1, 0)
        self.assertEqual(self.game.ties, 1)

        self.assertEqual(self.game.new_game_is_needed, True)

    def test_game_ends_player_1_capture_more_than_half(self):
        self.assertEqual(self.game.player_turn, True)
        self.game.kalah_board = [
            0, 0, 1, 0, 5, 6, 24,
            1, 2, 3, 1, 5, 6, 7,

        ]
        self.assertEqual(self.game.new_game_is_needed, False)
        self.game.play(2)
        self.game.kalah_board = [
            0, 0, 0, 0, 5, 6, 26,
            1, 2, 3, 0, 5, 6, 7,

        ]
        self.assertEqual(self.game.player_2, 0)
        self.assertEqual(self.game.player_1, 1)
        self.assertEqual(self.game.ties, 0)
        self.assertEqual(self.game.new_game_is_needed, True)

    def test_game_ends_player_2_capture_more_than_half(self):
        self.assertEqual(self.game.player_turn, True)
        self.game.kalah_board = [
            1, 2, 3, 1, 5, 6, 7,
            0, 0, 1, 0, 5, 6, 24,
        ]
        self.game.player_turn = not self.game.player_turn
        self.assertEqual(self.game.player_turn, False)

        self.game.play(2)
        self.game.kalah_board = [
            1, 2, 3, 0, 5, 6, 7,
            0, 0, 0, 0, 5, 6, 26,
        ]
        self.assertEqual(self.game.player_2, 1)
        self.assertEqual(self.game.player_1, 0)
        self.assertEqual(self.game.ties, 0)

        self.assertEqual(self.game.new_game_is_needed, True)


if __name__ == '__main__':
    unittest.main()
