from abc import ABC, abstractmethod


class PaymentStrgy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
