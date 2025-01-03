from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, temp, humidity):
        pass

    def shutdown(self):
        pass