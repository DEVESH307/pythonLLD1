from abc import ABC, abstractmethod


class Winning(ABC):

    @abstractmethod
    def check_winner(self, board, cell):
        pass

    @abstractmethod
    def handle_undo(self, board, cell):
        pass
