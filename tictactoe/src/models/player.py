from tictactoe.src.models.cellStatus import CellStatus


class Player:
    def __init__(self, name, type, id, symbol):
        self.name = name
        self.type = type
        self.id = id
        self.symbol = symbol

    def decide_cell(self, board):
        while True:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board.grid[row][col].status == CellStatus.EMPTY:
                    return board.grid[row][col]

            print("Invalid row or column")
