from tictactoe.src.CustomExceptions.InvalidPlayerException import InvalidPlayerException
from tictactoe.src.models.board import Board


class GameBuilder:
    def __init__(self):
        self.dimensions = None
        self.players = None
        self.winning_strgy = None

    def set_dimensions(self, dimensions):
        self.dimensions = dimensions
        return self

    def set_players(self, players):
        self.players = players
        return self

    def set_winning_strgy(self, winning_strgy):
        self.winning_strgy = winning_strgy
        return self


    def validate(self):
        if len(self.players) > self.dimensions-1:
            raise InvalidPlayerException()

    #     Other...

    def build(self):
        from tictactoe.src.models.Game import Game

        self.validate()
        return Game(Board(self.dimensions), self.players, self.winning_strgy)


