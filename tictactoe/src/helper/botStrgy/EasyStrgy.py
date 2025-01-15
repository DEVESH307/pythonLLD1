from tictactoe.src.models.cellStatus import CellStatus


class EasyStrgy:
    def decide_move(self, board):
        for row in board.grid:
            for cell in row:
                if cell.status == CellStatus.EMPTY:
                    return cell

        return None