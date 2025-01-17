from tictactoe.src.controllers.gameController import GameController
from tictactoe.src.helper.winningStrgy.diagonalWS import DiagonalWS
from tictactoe.src.models.GameStatus import GameStatus
from tictactoe.src.models.BotDificulty import BotDificulty
from tictactoe.src.models.PlayerType import PlayerType
from tictactoe.src.models.bot import Bot
from tictactoe.src.models.player import Player
from tictactoe.src.models.symbol import Symbol

if __name__ == '__main__':
    gc = GameController()

    dimension = 3

    players = [
        Player("karan", PlayerType.HUMAN, 1, Symbol('x')),
        Bot(2, "Bot", Symbol('y'), BotDificulty.EAZy)
    ]

    winning = [DiagonalWS()]

    game = gc.start_game(dimension, players, winning)

    while game.gameStatus == GameStatus.INPROGRESS:
        gc.take_turn(game)
        gc.display_board(game)
        if game.gameStatus ==  GameStatus.INPROGRESS:
            undoAnswer = input("Do you want to undo the last move? (1/0) ")
            if undoAnswer == "1":
                print("Undoing..")
                gc.undo_move(game)
                gc.display_board(game)

    if game.gameStatus == GameStatus.COMPLETE:
        print(f"Winner: {game.winner.name}")

    else:
        print("DRAW...")