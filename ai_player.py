import random

from player import Player


class AIPlayer(Player):

    def __int__(self, board, color):
        super.__init__(board, color)

    def move(self):
        move = random.choice(list(self.board.legal_moves))
        self.evaluate()
        self.perform_move(move)

    def evaluate(self):
        moves = list(self.board.legal_moves)

        print(moves[0])





