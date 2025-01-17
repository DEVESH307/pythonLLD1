from tictactoe.src.service.GameService import GameService


class GameController:

    def __init__(self):
        self.gameService = GameService()
    def start_game(self, size, players, winning):
        return self.gameService.start_game(size, players, winning)

    def display_board(self, game):
        self.gameService.display_board(game)

    def take_turn(self, game):
        self.gameService.take_turn(game)


    def undo_move(self, game):
        self.gameService.undo(game)



# start game
# intially status is inProgress
# IN LOOP:
#      display board
#      take input for move
#      check winner
#      if no winner and cells are still empty:
#           give turn to other player
#           Loop:
