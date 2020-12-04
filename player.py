from abc import ABC

import chess

MATERIAL_SCORE = {
    chess.PAWN: 10,
    chess.KNIGHT: 30,
    chess.BISHOP: 30,
    chess.ROOK: 50,
    chess.QUEEN: 90,
    chess.KING: 900,
}


class Player(ABC):

    def __init__(self, board, color):
        self.board = board
        self.color = color

    def move(self):
        raise NotImplemented

    def perform_move(self, uci_move):
        self.board.push(uci_move)
        print(f"{self.get_color()} moved {uci_move}")

    def get_color(self):
        return "WHITE" if self.color == chess.WHITE else "BLACK"

    def calculate_fitness(self):

        score = 0

        for piece, value in MATERIAL_SCORE.items():
            squares = self.board.pieces(piece, self.color)
            score += value * len(squares)

        return score

