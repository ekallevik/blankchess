import chess
import random
from abc import ABC


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


class HumanPlayer(Player):

    def __int__(self, board, color):
        super.__init__(board, color)

    def move(self):
        valid_move = False

        while not valid_move:
            move = input("Choose a move: ")
            if chess.Move.from_uci(move) in self.board.legal_moves:
                self.perform_move(chess.Move.from_uci(move))
                valid_move = True
            else:
                print(f"{move} is invalid")


class AIPlayer(Player):

    def __int__(self, board, color):
        super.__init__(board, color)

    def move(self):
        move = random.choice(list(self.board.legal_moves))
        self.perform_move(move)


def play():

    board = chess.Board()
    white = HumanPlayer(board, chess.WHITE)
    black = AIPlayer(board, chess.BLACK)

    current_player = white

    while not board.is_game_over(claim_draw=False):
        print(board)
        print(f"{current_player.get_color()} to move.")
        current_player.move()
        current_player = black if current_player == white else white
        print()


if __name__ == '__main__':
    play()

