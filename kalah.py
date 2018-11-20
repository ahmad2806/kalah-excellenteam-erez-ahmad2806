class Kalah(object):
    def __init__(self, holes, seeds):
        self.kalah_board = [seeds if not i == holes and not i == ((holes * 2) + 1) else 0 for i in
                            range(0, (holes * 2) + 2)]

