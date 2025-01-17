from tictactoe.src.helper.GameBuilder import GameBuilder
from tictactoe.src.models.GameStatus import GameStatus
from tictactoe.src.models.cellStatus import CellStatus


class GameService:

    def start_game(self, size, players, winning):
        game = (GameBuilder().set_players(players).
                set_dimensions(dimensions=size).set_winning_strgy(winning).build())

        return game

    def display_board(self, game):
        game.board.print_board()

    def take_turn(self, game):
        current_player = game.players[game.curr_turn]
        cell = current_player.decide_cell(game.board)
        cell.player = current_player
        cell.status = CellStatus.FILLED

        game.moves.append(cell)

        if self.check_winner(game, cell):
            game.winner = current_player
            game.gameStatus = GameStatus.COMPLETE

        elif len(game.moves) == game.board.board_size * game.board.board_size:
            game.gameStatus = GameStatus.DRAW

        game.curr_turn += 1
        game.curr_turn %= len(game.players)

    def check_winner(self, game, cell):
        for win in game.winning_statergies:
            if win.check_winner(game.board, cell):
                return True
        return False

    # any(win.check_winner(game.board, cell) for win in game.winning_statergies)

    def undo(self, game):
        if not game.moves:
            print("Nothing to undo")
            return

        cell = game.moves.pop()


        for win in game.winning_statergies:
            win.handle_undo(cell, game.board)

        cell.status = CellStatus.EMPTY
        cell.player = None
        game.curr_turn -= 1
        game.curr_turn %= len(game.players)
