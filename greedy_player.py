import random
import time

from player import Player


class GreedyPlayer(Player):

    def __int__(self, board, color, timeout):
        super.__init__(board, color)
        self.timeout = timeout

    def move(self):
        move = random.choice(list(self.board.legal_moves))
        time.sleep(self.timeout)
        self.perform_move(move)
