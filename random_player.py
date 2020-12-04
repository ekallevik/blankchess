import random
import time

from player import Player


class RandomPlayer(Player):

    def __int__(self, board, color):
        super.__init__(board, color)

    def move(self):
        move = random.choice(list(self.board.legal_moves))
        time.sleep(1)
        self.perform_move(move)
