from abc import ABC, abstractmethod


class checkbox(ABC):
    @abstractmethod
    def click(self):
        pass