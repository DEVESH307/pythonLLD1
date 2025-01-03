from abc import ABC, abstractmethod


class BankAdapterABC(ABC):

    @abstractmethod
    def checkBalance(self) -> int:
        pass