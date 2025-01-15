from tictactoe.src.helper.botStrgy.EasyStrgy import EasyStrgy
from tictactoe.src.models.BotDificulty import BotDificulty


class BotFactory:

    @staticmethod
    def createBot(dificulty):
        if dificulty == BotDificulty.EAZy:
            return EasyStrgy()