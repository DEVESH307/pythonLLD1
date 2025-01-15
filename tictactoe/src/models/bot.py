from tictactoe.src.helper.BotFactory import BotFactory
from tictactoe.src.models.PlayerType import PlayerType
from tictactoe.src.models.player import Player


class Bot(Player):
    def __init__(self, player_id: int, name: str, symbol, difficulty):
        super().__init__(name, player_id, PlayerType.BOT, symbol)
        self.difficulty = difficulty
        self.strgy = BotFactory.createBot(difficulty)


    def decide_cell(self, board):
        return self.strgy.decide_move(board)