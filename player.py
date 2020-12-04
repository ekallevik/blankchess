from abc import ABC

import chess


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