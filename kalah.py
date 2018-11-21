class Kalah(object):
    def render(self):
        rendered = ""
        player1_holes = " | ".join(str(h) for h in self.kalah_board[0: self.holes_count])
        player2_holes = " | ".join(str(h) for h in self.kalah_board[self.holes_count + 1: len(self.kalah_board) - 1])
        player1_holes = "| | " + player1_holes + " | |"
        player2_holes = "| | " + player2_holes + " | |"
        vertical_separator = \
            f'|{self.kalah_board[self.player_two_bank]}|' + \
            ('-' * (self.holes_count * 3 + 5)) + \
            f'|{self.kalah_board[self.player_one_bank]}|'

        rendered += "\n\n"
        rendered += "Player 2".center(len(vertical_separator)) + "\n"
        rendered += player2_holes + "\n"
        rendered += vertical_separator + "\n"
        rendered += player1_holes + "\n"
        rendered += "Player 1".center(len(vertical_separator)) + "\n"

        return rendered

    def __repr__(self):
        my_string = ""

        my_string += "Kalah("
        my_string += f"{str(self.start_seeds)}, {str(self.holes_count)}, status="

        my_string += str(tuple(self.kalah_board))
        my_string += ", player = "
        if self.player_turn:
            my_string += "1)"
        else:
            my_string += "2)"
        return my_string

    def __str__(self):
        return self.render()

    def __init__(self, holes, seeds):
        self.kalah_board = [seeds if not i == holes and not i == ((holes * 2) + 1) else 0 for i in
                            range(0, (holes * 2) + 2)]
        self.player_1 = 0
        self.player_2 = 0
        self.ties = 0
        self.holes_count = holes
        self.start_seeds = seeds
        self.new_game_is_needed = False
        self.player_one_bank = holes
        self.player_two_bank = holes * 2 + 1
        self.player_turn = True  # true for player one and false for player two turn

    def play(self, hole):
        if self.new_game_is_needed:
            print("game has ended, Please start new one")
            print(f"score : player 1 = {self.player_1},  player 2 : {self.player_2}")
        if hole < 0 or hole >= self.holes_count or hole == self.player_two_bank or hole == self.player_two_bank:
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

        hole = self.move(hole, my_seeds, other_bank)
        hole = self.capture_seeds(hole, player_bank, other_bank)

        is_winner = self.check_for_winner(player_bank, True)
        if not is_winner:
            game_end = \
                self.game_has_ended(0, player_bank) if self.player_turn else self.game_has_ended(other_bank + 1,
                                                                                                 player_bank)
            if game_end:
                self.get_points(player_bank + 1, other_bank) \
                    if self.player_turn else self.get_points(0, other_bank)
                if self.kalah_board[player_bank] == self.kalah_board[other_bank]:
                    print("TIE")
                    self.ties += 1
                    self.new_game_is_needed = True

                self.check_for_winner(other_bank, False)
        if hole != player_bank:
            self.player_turn = not self.player_turn

    def capture_seeds(self, hole, player_bank, other_bank):
        if self.kalah_board[hole] == 1:
            if hole < player_bank:
                points = 1
                points += self.kalah_board[other_bank - self.holes_count + hole]
                if points == 1:  # cell in the line before was empty
                    return hole
                self.kalah_board[hole] = 0
                temp = 0
                if hole / self.holes_count < 1:
                    temp = other_bank - self.holes_count + hole
                else:
                    temp = other_bank - self.holes_count + (hole % self.holes_count) - 1
                self.kalah_board[temp] = 0
                self.kalah_board[player_bank] += points
                return player_bank
        return hole

    def move(self, hole, my_seeds, other_bank):
        for amount in range(my_seeds):
            if hole == other_bank:
                hole += 1
            if hole > self.player_two_bank:
                hole = 0

            self.kalah_board[hole] += 1
            hole += 1
        hole -= 1
        return hole

    def game_has_ended(self, start_index, end_index):
        for cell in range(start_index, end_index):
            if self.kalah_board[cell] != 0:
                return False
        return True

    def get_points(self, start_index, end_index):

        for cell in range(start_index, end_index):
            self.kalah_board[end_index] += self.kalah_board[cell]
            self.kalah_board[cell] = 0

    def check_for_winner(self, bank_to_check, player_playing):
        if self.kalah_board[bank_to_check] > self.holes_count * self.start_seeds:

            if player_playing:
                if self.player_turn:
                    self.player_1 += 1
                    print("PLAYER 1 WIN!")
                else:
                    self.player_2 += 1
                    print("PLAYER 2 WIN!")
            else:
                if not self.player_turn:
                    self.player_1 += 1
                    print("PLAYER 1 WIN!")
                else:
                    self.player_2 += 1
                    print("PLAYER 2 WIN!")
            self.new_game_is_needed = True
            return True
        return False



