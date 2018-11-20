class Kalah(object):
    def __init__(self, holes, seeds):
        self.kalah_board = [seeds if not i == holes and not i == ((holes * 2) + 1) else 0 for i in
                            range(0, (holes * 2) + 2)]
        self.player_1 = 0
        self.player_2 = 0
        self.holes_count = holes;
        self.player_one_bank = holes
        self.player_two_bank = holes * 2 + 1
        self.player_turn = True

    def play(self, hole):
        if hole < 0 or hole > self.holes_count:
            print("illegal hole number")
            return

        my_seeds = self.kalah_board[hole]
        self.kalah_board[hole] = 0
        hole += 1

        for amount in range(my_seeds):
            self.kalah_board[hole] += 1
            hole += 1
