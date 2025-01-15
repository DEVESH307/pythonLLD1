from tictactoe.src.models.GameStatus import GameStatus


class Game:
    def __init__(self, board, players, winning_statergies):
        self.board = board
        self.players = players
        self.winning_statergies = winning_statergies
        self.moves = []
        self.curr_turn = 0
        self.winner = None
        self.gameStatus = GameStatus.INPROGRESS