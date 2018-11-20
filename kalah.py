class Kalah(object):
    def __init__(self, holes, seeds):
        self.kalah_board = [seeds if not i == holes and not i == ((holes * 2) + 1) else 0 for i in
                            range(0, (holes * 2) + 2)]
        self.player_1 = 0
        self.player_2 = 0
        self.holes_count = holes;
        self.player_one_bank = holes
        self.player_two_bank = holes * 2 + 1
        self.player_turn = True  # true for player one and false for player two turn

    def play(self, hole):
        if hole < 0 or hole > self.holes_count or hole == self.player_two_bank or hole == self.player_two_bank:
            print("illegal hole number")
            return

        if not self.player_turn:  # player two turn start counting from his bank
            hole += (self.player_one_bank + 1)

        if self.kalah_board[hole] == 0:
            print("cell is empty, please try again")
            return

        my_seeds = self.kalah_board[hole]
        self.kalah_board[hole] = 0
        hole += 1

        player_bank = self.player_one_bank if self.player_turn else self.player_two_bank
        other_bank = self.player_one_bank if not self.player_turn else self.player_two_bank
        for amount in range(my_seeds):
            if hole == other_bank:
                hole += 1
            if hole > self.player_two_bank:
                hole = 0

            self.kalah_board[hole] += 1
            hole += 1

        if hole - 1 != player_bank:
            self.player_turn = not self.player_turn












