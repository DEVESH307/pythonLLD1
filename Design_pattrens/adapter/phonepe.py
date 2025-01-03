from Design_pattrens.adapter.adapters.BankAdapterABC import *


class Phonepe:
    def __init__(self, Adapter: BankAdapterABC):
        self.Adapter = Adapter

    def checkBalance(self):
        return self.Adapter.checkBalance()
