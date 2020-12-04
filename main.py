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


class Game:

    def __init__(self, starting_player):

        self.board = chess.Board()
        self.human = HumanPlayer(self.board, chess.WHITE if starting_player == "human" else chess.BLACK)
        self.ai = AIPlayer(self.board, chess.BLACK if starting_player == "human" else chess.WHITE)

        self.current_player = self.human if starting_player == "human" else self.ai

    def play(self):
        while not self.board.is_game_over(claim_draw=False):
            print(self.board)
            print(f"{self.current_player.get_color()} to move.")
            self.current_player.move()
            self.update_current_player()
            print()

    def update_current_player(self):
        self.current_player = self.ai if self.current_player == self.human else self.human

if __name__ == '__main__':
    game = Game("human")
    game.play()


