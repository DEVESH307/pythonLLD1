from tictactoe.src.helper.GameBuilder import GameBuilder


class GameService:

    def start_game(self, size, players, winning):
        game = (GameBuilder().set_players(players).
                set_dimensions(dimensions=size).set_winning_strgy(winning).build())

        return game

    def display_board(self, game):
        game.board.print_board()


    def take_turn(self, game):
        current_player = game.players[game.curr_turn]

