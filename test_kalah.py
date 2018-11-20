import unittest
from kalah import Kalah


class KalahTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Kalah(6, 4)
        self.game1 = Kalah(5, 5)

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(self.game.mancala_board, [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.assertEqual(self.game1.mancala_board, [5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0])


if __name__ == '__main__':
    unittest.main()
