import chess

from ai_player import AIPlayer
from human_player import HumanPlayer


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
