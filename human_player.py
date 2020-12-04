import chess

from player import Player


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