import chess

from ai_player import AIPlayer
from human_player import HumanPlayer
from random_player import RandomPlayer


class Game:

    def __init__(self, board, white, black):
        self.board = board
        self.white = white
        self.black = black

        self.current_player = self.white

    def play(self):
        while not self.board.is_game_over(claim_draw=False):
            print(self.board)
            print(f"{self.current_player.get_color()} to move.")
            self.current_player.move()
            self.update_current_player()
            print()

        print("### GAME OVER ###")

    def update_current_player(self):
        self.current_player = self.get_next_player()

    def get_next_player(self):
        return self.black if self.current_player == self.white else self.white


def setup_and_play():
    board = chess.Board()
    white = RandomPlayer(board, chess.WHITE)
    black = RandomPlayer(board, chess.BLACK)
    game = Game(board, white, black)
    game.play()


if __name__ == '__main__':
    setup_and_play()
